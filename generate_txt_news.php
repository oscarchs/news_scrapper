<?php
$servername = "database-1.c7bfmd9vlb4s.us-east-1.rds.amazonaws.com";
$username = "admin";
$password ="MAhm6vOGUsDkKsdNmHaT";

// Create connection
$conn = new mysqli($servername, $username, $password, 'search_engine_dataset');

// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}; 

$data_chunk = $conn->query("SELECT * FROM news_dataset;");


/*foreach($data_chunk as $record){
  echo $record['url']."\n";
  echo $record['headline']."\n";
  echo html_entity_decode($record['content'])."\n";
  echo "-------------------------------------------------------------------------------\n";
}*/


foreach($data_chunk as $record){
  file_put_contents(strval($record['id']).'.txt', html_entity_decode($record['content']));
}
?>
