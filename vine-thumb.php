<?php

include 'inc/functions.php';

$video_id = filter_var(basename($_SERVER['REQUEST_URI']), FILTER_SANITIZE_STRING);
$image_found = false;


preg_match('/[a-zA-Z0-9]{10,15}/', $video_id, $matches);


if ($matches[0] !== false) {
	$filename = md5($video_id) .'.jpg';

	if (!showImage($filename)) {
		$data = read('https://api.vineapp.com/timelines/posts/s/'. $video_id);

		if (in_array('records', $data) &&
			!empty($data['data']['records'])) {
			
			$thumbnail_url = $data['data']['records'][0]['thumbnailUrl'];

			if (saveImage($thumbnail_url, $filename)) {
				showImage($filename);

				$image_found = true;
			}
		}
	} else {
		$image_found = true;
	}
}

if (!$image_found) {
	showImage('../blank.jpg');
}