<?php

error_reporting(E_ALL);
ini_set('display_errors', '1');

function cURL($url) {
    $ch = curl_init();

    curl_setopt_array($ch, array(
        CURLOPT_FOLLOWLOCATION => true,
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_URL => $url
    ));

    $data = curl_exec($ch);
    curl_close($ch);

    return $data;
}

function saveImage($url, $destination) {
    if (!imageExists($destination)) {
        $data = cURL($url);
        
        $fp = fopen('files/'. $destination, 'x');
        fwrite($fp, $data);
        fclose($fp);

        if (imageExists($destination)) {
            return true;
        }
    } else {
        return true;
    }
}

function read($url) {
    $data = cURL($url);

    if ($data) {
        return json_decode($data, true);
    }
}

function showImage($filename) {
    if (imageExists($filename)) {
        header('Content-type: image/jpeg');
        readfile('files/'. $filename);
        
        exit(0);
    }

    return false;
}

function imageExists($filename) {
    return file_exists('files/'. $filename);
}