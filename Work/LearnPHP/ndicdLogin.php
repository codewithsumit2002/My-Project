<?php
    include 'ndicdConnection.php';
?>
<!DOCTYPE html>
<html lang="en">

<head>
    <title>Log In</title>
    <link rel="stylesheet" type="text/css" href="ndicdStyle.css">
    <link rel="stylesheet" type="text/css" href="ndicdReg.css">
    <link rel="stylesheet" type="text/css" href="ndicdLogin.css">

</head>

<body>

<div class="wrapper">
    <div class="wrapper1">
        <div>
                <div class="address">&#x1F4CD; NDICD Building Udhyog Nagar, Naini, Prayagraj,Utter Pradesh, 211008</div>
                <div class="head">
                    <h1><strong>Naurangi Devi Institute of Career & Development</strong></h1>
                </div>
                <div class="nav">
                    <ul class="nav-list">
                        <li><a href="ndicdMain.php" name="home">Home</a></li>
                        <li>
                            <a href="#" name="aboutus">About Us</a>
                            <ul class="submenu">
                                <li><a href="#">Mission</a></li>
                                <li><a href="#">Team</a></li>
                                <li><a href="#">History</a></li>
                            </ul>
                        </li>
                        <li>
                            <a href="ndicdCourse.php" name="courses">Courses</a>

                        </li>
                        <li>
                            <a href="#" name="placement">Placement</a>
                            <ul class="submenu">
                                <li><a href="#">Placement Statistics</a></li>
                                <li><a href="#">Placement Process</a></li>
                                <li><a href="#">Placement Partners</a></li>
                            </ul>
                        </li>
                        <li>
                            <a href="#" name="contactus">Contact Us</a>
                            <ul class="submenu">
                                <li><a href="#"> Phone: +91 969 661 3889</a></li>
                                <li><a href="mailto:ndicd.prayagraj@gmail.com">ndicd.prayagraj@gmail.com</a></li>
                            </ul>
                        </li>
                        <li><a href="ndicdResult.php" name="result" target="_blank">Result</a></li>
                        <li><a href="ndicdReg.php" name="register" target="_blank">Register</a></li>
                        <li><a href="ndicdLogin.php" name="login" target="_blank">Log In</a></li>

                    </ul>
                </div>


                <!--Body Content-->
                <div class="container">
                    <h1>Log In Form</h1>
                    <form id="registration-form" action="<?php echo $_SERVER['PHP_SELF']; ?>" method="POST">
                        <div class="form-group">
                            <label for="name">Name:</label>
                            <input type="text" id="name" name="name" placeholder="Enter Your Full Name..." required>
                        </div>

                        <div class="form-group">
                            <label for="email">Email:</label>
                            <input type="email" id="email" name="email" placeholder="example@gmail.com" required>
                        </div>

                        <div class="form-group">
                            <label for="password">Password:</label>
                            <input type="password" id="password" name="password" placeholder="Enter Your Password"
                                required>
                        </div>
                        <div class="form-group">
                            <label for="conpassword">Confirm Password:</label>
                            <input type="password" id="conpassword" name="conpassword"
                                placeholder="confirm Your Password" required>
                        </div>

                        <div class="form-group">
                            <label for="phone">Phone:</label>
                            <input type="tel" id="phone" name="phone" value="+91 " required>
                        </div>


                        <div class="buttonsMain">
                            <div class="buttons">
                                <input type="submit" name="register" value="Register">
                            </div>
                            <div class="buttons">
                                <input type="submit" value="Cancle">
                            </div>
                            <div class="buttons">
                                <input type="reset" value="Reset">
                            </div>

                            <div class="user">
                                <div class="buttons">
                                    New User?
                                </div>
                                <div class="buttons">
                                    <a href="ndicdReg.php" target="_blank">Register here</a>
                                </div>
                            </div>
                        </div>
                    </form>
                </div>
        </div>

        <footer class="footer">
                <!--Footer Content-->
                <div class="wrapper">
                    <div class="footer-content">
                        <div class="footer-section">
                            <h3>About Us</h3>
                            <p>Naurangi Devi Institute of Career & Development is a leading educational institution
                                dedicated to providing
                                quality education and career development opportunities.</p>
                        </div>
                        <div class="footer-section">
                            <h3>Quick Links</h3>
                            <ul>
                                <li><a href="ndicdMain.php">Home</a></li>
                                <li><a href="ndicdCourse.php">Courses</a></li>
                                <li><a href="ndicdResult.php">Result</a></li>
                                <li><a href="ndicdReg.php">Register</a></li>
                                <li><a href="ndicdLogin.php">Log In</a></li>
                            </ul>
                        </div>
                        <div class="footer-section">
                            <h3>Contact Us</h3>
                            <p>
                                Address: NDICD Building Udhyog Nagar, Naini, Prayagraj,Utter Pradesh, 211008<br><br>
                                Phone: +91 9696613889 <br>
                                Email: <a href="mailto:info@ndicd.edu">ndicd.prayagraj@gmail.com</a>
                            </p>
                        </div>
                        <div class="footer-section" id="footer-section">
                            <h3>Follow Us</h3>
                            <ul>
                                <li class="fla1"><a href="https://www.facebook.com/neeraj.jais" target="_blank">facebook
                                        <i class="fa fa-facebook"></i></a></li>&nbsp;
                                <li class="fla2"><a href="https://www.instagram.com/ndicd.naini"
                                        target="_blank">Instagram <i class="fa fa-twitter"></i></a></li>&nbsp;
                                <li class="fla3"><a href="#" target="_blank">Twitter <i class="fa fa-instagram"></i></a>
                                </li>&nbsp;
                                <li class="fla4"><a href="#" target="_blank">LinkedIn <i class="fa fa-linkedin"></i></a>
                                </li>&nbsp;
                                <li class="fla5"><a href="#" target="_blank">Youtube<i class="fa fa-youtube"></i></a>
                                </li>&nbsp;
                            </ul>
                        </div>

                    </div>
                    <div class="footer-copyright">
                        <p>&copy; 2024 Naurangi Devi Institute of Career & Development. All rights reserved.</p>
                    </div>
                    <div class="tag">Made with ❤️ By
                        <span>Sumit</span>
                    </div>
                </div>
        </footer>
    </div>
</div>

</body>

</html>
<?php
    echo "database working properly";
    
        // code...
    
    if ($_POST['register']) {
        $name=$_POST['name'];
        $email=$_POST['email'];
        $pwd=$_POST['password'];
        $cpwd=$_POST['conpassword'];        
        $phone=$_POST['phone'];
       
        if ($pwd==$cpwd) {
            $query="INSERT INTO ndicd_login VALUES('$name','$email','$pwd','$cpwd','$phone')";
            $data=mysqli_query($conn,$query);
            if ($data) {
                echo "Data inserted into Log in database";
            }
            else{
                echo "Failed";
            }

        }

        else{
            echo "password are  not same";
        }
    }
?>