<?php 
$servername = "localhost";
$username = "oscar";
$password ="chujutalli";

// Create connection
$conn = new mysqli($servername, $username, $password, 'search_engine_dataset');

// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}; 

$data_chunk = $conn->query("SELECT * FROM news_dataset limit 10;");


foreach($data_chunk as $record){
  echo $record['url']."\n";
  echo $record['headline']."\n";
  echo $record['content']."\n";
  echo "-------------------------------------------------------------------------------";
}

$websites = [
  'https://rpp.pe/archivo/2019-02-02'
];

function get_news_content($url){
  $source_html = file_get_contents($url);
  $content_start =  strpos($source_html, 'articleBody": "') + 15;
  $content_end = strpos($source_html, '",', $content_start) - $content_start;

  $headline_start = strpos($source_html, 'headline": "') + 12;
  $headline_end = strpos($source_html, '",', $headline_start) - $headline_start;
  return [ 'content' => str_replace("'", "''", substr($source_html, $content_start, $content_end)), 
            'headline' => substr($source_html, $headline_start, $headline_end)];
}

function run($websites, $conn){
  $heading_html_piece = 'cont">';
  $source_html = file_get_contents($websites[0]);
  $dom = new domDocument;
  $dom->loadHtml($source_html);

  $finder = new DomXPath($dom);
  //$nodes = $finder->query('//tr[@class="cont"]');
  $classname = "cont";
  $nodes = $finder->query("//*[contains(@class, '$classname')]");

  foreach($nodes as $node){
    if($node->childNodes && sizeof($node->childNodes) > 2){
      $a_element = $node->childNodes[1]->firstChild;
      if(isset($a_element->attributes) && sizeof($a_element->attributes) > 0 && $a_element->attributes[0]->name == 'href'){
        $url = $a_element->attributes[0]->value;
        $contents = get_news_content($url);
        $contents['url'] = $url;
        $query = "INSERT INTO news_dataset(headline, url, content) values('".$contents['headline']."', '".$contents['url']."', '".$contents['content']."')";
        $conn->query($query);
        echo $conn->error;
        print_r($contents);
        echo $query;
        break;
      }
    }
  }
}

run($websites, $conn);

?>
