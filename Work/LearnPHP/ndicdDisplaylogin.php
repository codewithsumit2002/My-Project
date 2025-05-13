
<?php
	include 'ndicdConnection.php';

	$query="SELECT * FROM ndicd_login";
	$data=mysqli_query($conn,$query);

	$total=mysqli_num_rows($data);
	$result=mysqli_fetch_assoc($data);
	//echo $total;
	/*
	$dis= $result['name']." ".$result['email']." ".$result['password']." ".$result['conpasssword']." ".$result['phone'];
	echo "<br>".$dis."<br>";
	*/
    echo "<br>";
	if($total!=0){
        while($result=mysqli_fetch_assoc($data)){

            echo "<br>".$result['name']." ".$result['email']." ".$result['password']." ".$result['confirm password']." ".$result['phone']."<br>";
        }
		echo "<br>Table has records from ndicd_displaylogin.php file<br>";

	} 
	else{
		echo "No rcord founds";
	}

?>