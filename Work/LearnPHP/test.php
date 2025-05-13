<?php
$data="hello";
$filepath='datatest.txt';
if (file_exists($filepath)) {
	// code...
	echo "file exists";

if (file_put_contents($filepath, $data,FILE_APPEND)) {
	// code...
	echo "Data writte successfully";
} else {
	// code...
	echo "Error data writting  into file";
}}
else{
	echo "file does not exists";
}

?>