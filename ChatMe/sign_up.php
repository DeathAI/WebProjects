<!DOCTYPE html>
<html>
<head>
	<title>Login Page</title>
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<link rel="stylesheet" href="css/style.css">
	<link rel="stylesheet" href="css/bootstrap.css">
</head>
<body> 
	<div class="login-box">
		<h1>Sign Up</h1>
		<form action="" method="post">
			<div class="user-box">
				<p id="lb0" class="inline">User Name</p>
				<input type="text" id="UserName" name="UserName" placeholder="User Name" required>
			</div>
			<div class="user-box">
				<p id="lb1" class="inline">Email</p>
				<input type="email" id="mail" name="email" placeholder="Email" required>
			</div>
			<div class="user-box">
				<p id="lb2" class="inline">Password</p>
				<input type="password" name="password" id="password" placeholder="password" required>
			</div>
			<div class="user-box">
				<p id="lb3" class="inline">Conform Password</p>
				<input type="password" name="cPassword" id="cPassword" placeholder="Conform Password" required>
			</div>
			<center>
				<input class="btn btn-success mx-3 col-6" type="submit" value="Sign Up" name="Sub">
				<input onclick="document.location ='index.html'; " class="btn btn-danger col-6" type="submit" value="HOME" name="Sub">
			</center>
			</form>
			<?php
				if(isset($_POST["Sub"])){
					$servername = "localhost";
					$username = "root";
					$password = "";
					$dbname = "chatme";
					$conn = new mysqli($servername, $username, $password, $dbname);
					$UserName = $_POST['UserName'];
					$id = $_POST['email'];
					$password = $_POST['password'];
					$cPassword = $_POST['cPassword'];
					if(str_replace(' ','',$UserName) === $UserName){
						if($cPassword === $password){
							// echo "$UserName   $id  $password";
							$query = "INSERT INTO `accounts`(`UserName`, `Mail_ID`, `Password`) VALUES ('$UserName','$id','$password')";
						 	if ($conn->query($query) === TRUE) {
								if($conn->query("CREATE TABLE rMsg_$UserName(From_ varchar(32), message varchar(2048), mID int(128) UNIQUE, rTo int(128), mTime TIMESTAMP DEFAULT CURRENT_TIMESTAMP)") === TRUE){
									if($conn->query("CREATE TABLE sMsg_$UserName(To_ varchar(32), message varchar(2048), mID int(128) UNIQUE, rTo int(128), status int(1), mTime TIMESTAMP DEFAULT CURRENT_TIMESTAMP)") === TRUE){
										if ($conn->query("CREATE TABLE friends_$UserName(UID int(16) UNIQUE, UserName varchar(32) UNIQUE, Mail_ID varchar(64) UNIQUE, chatScore int(16))") === TRUE) {
											setcookie("user_id","$id",time() + (86400 * 30),"/");
											setcookie ("user_pswd","$password",time() + (86400 * 30),"/");
											echo "<script type='text/javascript'> document.location ='home.php'; </script>";
										}
									}
								}
							} else {
								echo "<script>alert('Error:  + $query + '\r\n' + $conn->error')</script>";
							}
							$conn->close();
						}
					}
				}
				?>
			<p>Already have an account? <a href="Index.html">Sign in</a></p>
	</div>
</body>
<script>
	const PhoneNoField = document.getElementById('PhoneNo');
	PhoneNoField.addEventListener('input', function(){
		const  lb0 = document.getElementById('lb0')
		if (this.value.length > 0) {
			lb0.style.display = "inline";
		} else {
			lb0.style.display = "none";
		}
	});

	const emailField = document.getElementById('mail');
	emailField.addEventListener('input', function(){
		const lb1 = document.getElementById('lb1')
		if (this.value.length > 0) {
			lb1.style.display = "inline";
		} else {
			lb1.style.display = "none";
		}
	});

	const passwordField = document.getElementById('password');
	passwordField.addEventListener('input', function(){
		const  lb2 = document.getElementById('lb2')
		if (this.value.length > 0) {
			lb2.style.display = "inline";
		} else {
			lb2.style.display = "none";
		}
	});

	const CPasswordField = document.getElementById('cPassword');
	CPasswordField.addEventListener('input', function(){
		const  lb2 = document.getElementById('lb3')
		if (this.value.length > 0) {
			lb2.style.display = "inline";
		} else {
			lb2.style.display = "none";
		}
	});

</script>
</html>
