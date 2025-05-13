<?php
//error_reporting(0);
	$servername="localhost";
	$username="root";
	$password="";
	$dbname="ndicddb";

	$conn=mysqli_connect($servername,$username,$password,$dbname);
	if ($conn) {
		// code...
		echo  "Connection Established form ndicdconnection.php file";
	}
	else{
		echo  "Connection Failed".mysqli_connect_error();
	}

?>