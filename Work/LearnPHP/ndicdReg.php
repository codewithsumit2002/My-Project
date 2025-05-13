<?php
    include 'ndicdConnection.php';
?>
<!DOCTYPE html>
<html lang="en">

<head>
    <title>registration</title>

    <link rel="stylesheet" type="text/css" href="ndicdReg.css">
    <link rel="stylesheet" type="text/css" href="ndicdStyle.css">
    <script type="text/javascript">
    
    </script>
</head>

<body >

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
                <h1>Registration Form</h1>
                <form id="registration-form" action="ndicdReg.php" method="POST">
                    <div class="form-group">
                        <label for="name">Name:</label>
                        <input type="text" id="name" name="name" placeholder="Enter Your Full Name..." required>
                    </div>

                    <div class="form-group">
                        <label for="fname">Father's Name:</label>
                        <input type="text" id="fname" name="fname" placeholder="Enter Your Father's Name..." required>
                    </div>

                    <div class="form-group">
                        <label for="foc">Father's Occupation:</label>
                        <input type="text" id="foc" name="foc" placeholder="Enter Your Father's Occupation" required>
                    </div>
                    <div class="form-group">
                        <label for="gender">Gender:</label>

                        <select id="gender" name="gender">
                            <option>Select Gender</option>
                            <option>Male</option>
                            <option>Female</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label for="marital">Marital Status:</label>

                        <select id="marital" name="marital">
                            <option>Select Marital Status</option>
                            <option>Married</option>
                            <option>Unmarried</option>
                        </select>
                    </div>


                    <div class="form-group">
                        <label for="email">Email Id:</label>
                        <input type="email" id="email" name="email" placeholder="example@gmail.com" required>
                    </div>
                    <div class="form-group">
                        <label for="phone">Phone Number:</label>
                        <input type="tel" id="phone" name="phone" value="+91 " required>
                    </div>
                    <div class="form-group">
                        <label for="password">Password:</label>
                        <input type="password" id="password" name="password" required>
                    </div>

                    <div class="form-group">
                        <label for="course">Course:</label>
                        <input type="text" id="course" name="course" placeholder="Enter Course Name..." required>
                    </div>

                    <div class="form-group">
                        <label for="aadhar">Aadhar Number:</label>
                        <input type="tel" id="aadhar" name="aadhar" placeholder="Enter Your Aadhar Number" required>
                    </div>
                    <div class="form-group">
                        <label for="lqualification">Latest Qualification:</label>
                        <input type="tel" id="lqualification" name="lqualification"
                            placeholder="Enter Your Qualification" required>
                    </div>
                    <div class="form-group">
                        <label for="address">Address:</label>
                        <input type="text" id="text" name="address" required>
                    </div>

                    <div class="buttonsMain">
                        <div class="buttons">
                            <input type="submit" value="Register" name="register">
                        </div>
                        <div class="buttons">
                            <input type="submit" value="Cancel" name="cancel">
                        </div>
                        <div class="buttons">
                            <input type="reset" value="Reset" name="reset">
                        </div>

                        <div class="user">
                            <div class="buttons">
                                Already having account?
                            </div>
                            <div class="buttons">
                                <a href="ndicdLogin.php" target="_blank">Log in here</a>
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
                            <li class="fla1"><a href="https://www.facebook.com/neeraj.jais" target="_blank">facebook <i
                                        class="fa fa-facebook"></i></a></li>&nbsp;
                            <li class="fla2"><a href="https://www.instagram.com/ndicd.naini" target="_blank">Instagram
                                    <i class="fa fa-twitter"></i></a></li>&nbsp;
                            <li class="fla3"><a href="#" target="_blank">Twitter <i class="fa fa-instagram"></i></a>
                            </li>&nbsp;
                            <li class="fla4"><a href="#" target="_blank">LinkedIn <i class="fa fa-linkedin"></i></a>
                            </li>&nbsp;
                            <li class="fla5"><a href="#" target="_blank">Youtube<i class="fa fa-youtube"></i></a></li>
                            &nbsp;
                        </ul>
                    </div>

                </div>
                <div class="footer-copyright">
                    <p>&copy; 2024 Naurangi Devi Institute of Career & Development. All rights reserved.</p>
                </div>
                <div class="tag">Orgnaized and Maintained By
                    <span>Sumit</span>
                </div>
            </div>
            </footer>
    </div>
</div>

</body>
<script type="text/javascript">
    document.querySelector('button[name=cancel]').addEventListener('click',function(){
        window.location.href='ndicdMain.php';
        // body...
    });
</script>
</html>

<?php
    if ($_POST['register']) {
        $name=$_POST['name'];
        $fname=$_POST['fname'];
        $foc=$_POST['foc'];
        $gender=$_POST['gender'];
        $marital=$_POST['marital'];
        $email=$_POST['email'];
        $phone=$_POST['phone'];
        $pwd=$_POST['password'];
        $course=$_POST['course'];
        $aadhar=$_POST['aadhar'];
        $lq=$_POST['lqualification'];
        $address=$_POST['address'];

        $query="INSERT INTO ndicd_reg VALUES('$name','$fname','$foc','$gender','$marital','$email','$phone','$pwd','$course','$aadhar','$lq','$address')";
        $data=mysqli_query($conn,$query);
        if ($data) {
            echo "Data inserted into database";
        }
        else{
            echo "Failed";
        }

    }
?>
<?php
        if (isset($_POST['cancle'])) {
            // code...
            header('Location: ndicdMain.php');
            exit;
        }
?>