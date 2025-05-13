<?php
	include 'connection.php';

	$query="SELECT * FROM form";
	$data=mysqli_query($conn,$query);

	$total=mysqli_num_rows($data);
	$result=mysqli_fetch_assoc($data);
	//echo $total;
	
	$dis= $result['fname']." ".$result['lname']." ".$result['gender']." ".$result['email']." ".$result['phone']." ".$result['address'];
	echo "<br>".$dis."<br>";
	

	if($total!=0){
		echo "<br>Table has records from display.php file<br>";

	} 
	else{
		echo "No rcord founds";
	}

?>