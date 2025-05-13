
<?php
	include 'ndicdConnection.php';

	$query="SELECT * FROM ndicd_reg";
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

            echo "<br>".$result['name']." ".$result['fname']." ".$result['foc']." ".$result['gender']." ".$result['marital']." ".$result['email']." ".$result['phone']." ".$result['pwd']." ".$result['course']." ".$result['aadhar']." ".$result['lqualification']." ".$result['address']."<br>";
        }
		echo "<br>Table has records from ndicd_display.php file<br>";

	} 
	else{
		echo "No rcord founds";
	}

?>