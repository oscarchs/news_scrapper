<?php
require __DIR__ . '/vendor/autoload.php';
use voku\helper\StopWords;

$stopWords = new StopWords();
$stopWords = $stopWords->getStopWordsFromLanguage('es');


function clean(string $message, Array $stopWords): string{
    $message = sanitize($message);
    $iterable = mb_split("\s+", $message);

    foreach ($iterable as $pos => $item) {
        if (in_array(mb_strtolower($item), $stopWords) || mb_strlen(trim($item)) === 0) {
            unset($iterable[$pos]);
        }
    }

    return implode(' ', $iterable);
}

function sanitize(string $message): string{
    return mb_ereg_replace("/[^\p{L}\p{N}\_\s\-]/", " ", $message);
}

$dir = new DirectoryIterator('txtdataset');
foreach ($dir as $fileinfo) {
    if (!$fileinfo->isDot()) {
        $path = 'txtdataset/'.$fileinfo->getFilename();
        $content = clean(file_get_contents($path), $stopWords);
        file_put_contents($path, $content);
    }
}
?>