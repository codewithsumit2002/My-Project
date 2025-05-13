<?php
error_reporting(0);
	$servername="localhost";
	$username="root";
	$password="";
	$dbname="responsiveform3";

	$conn=mysqli_connect($servername,$username,$password,$dbname);
	if ($conn) {
		// code...
		echo  "Connection Established form connection.php file";
	}
	else{
		echo  "Connection Failed".mysqli_connect_error();
	}

?>