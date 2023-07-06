<!DOCTYPE html>
<html>
<head>
	<title>Login Page</title>
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<link rel="stylesheet" href="css/style.css">
	<link rel="stylesheet" href="css/bootstrap.css">
</head>
<style>
	.login-box { 
		width: 470px;
		height: 500px !important;
		background: #0000006b;
		color: #ffffff;
		top: 50%;
		left: 50%;
		position: absolute;
		transform: translate(-50%,-50%);
		padding:3% 0px 0px 0px;
		border-radius: 0% 20% 0% 20%;
		box-shadow: 0 5px 10px rgba(0,0,0,0.3);
	}
</style>
<body> 
	<div class="login-box">
		<h1>Login</h1>
		<form method="POST" action="insert_image.php" enctype="multipart/form-data">

			<div class="file-input">
			<label for="image">Select an image</label>
			<input type="file" name="image" id="image">
			</div>


			<input type="submit" value="Upload Image" name="Sub" class="btn btn-success mx-3">
			<?php
				if(isset($_POST["Sub"])){
					$servername = "localhost";
					$username = "root";
					$password = "";
					$dbname = "chatme";
					$conn = new mysqli($servername, $username, $password, $dbname,);
					$id = $_POST['email'];
					$password = $_POST['password'];
					$query = "SELECT * FROM `accounts` WHERE Mail_ID='$id'";
					
					$data = $conn->query($query);

					if ($data->num_rows > 0) {
						while($row = $data->fetch_assoc()) {
						  if($id == $row["Mail_ID"] && $password == $row["Password"]){
							setcookie("user_id","$id",time() + (86400 * 30),"/");
							setcookie ("user_pswd","$password",time() + (86400 * 30),"/");
							echo "<script type='text/javascript'> document.location ='home.php'; </script>";
						  }
						}
					}
					else {
						echo "<script>error('Email');</script>";
					}
					
					$conn->close();
					
				}
			?>
			<a href="#">Forgot Password?</a>
			<p>Don't have an account? <a href="Index.html">Sign Up</a></p>
		</form>
		<form action="LogOut.php" method="post">
			<input type="submit" value="Log out" name="Sub" class="btn btn-danger mx-3">
		</form>
	</div>
</body>
<script>
	const passwordField = document.getElementById('password');
	passwordField.addEventListener('input', function(){
		const  lb2 = document.getElementById('lb2')
		if (this.value.length > 0) {
			lb2.style.display = "inline";
		} else {
			lb2.style.display = "none";
		}
	});

	const emailField = document.getElementById('mail');
	const lb1 = document.getElementById('lb1')
	emailField.addEventListener('input', function(){
		if (this.value.length > 0) {
			lb1.style.display = "inline";
		} else {
			lb1.style.display = "none";
		}
	});
	function error(let name){
		let tmp = document.getElementById("error1");
		if(name == "Email"){
			let tmp.textContent = "User Name not Found";
		}
	}
</script>
</html>
