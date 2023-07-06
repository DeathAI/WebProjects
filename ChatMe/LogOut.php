<?php
    // Set expiration time to the past (e.g., 1 hour ago)
    $expiration_time = time() - 3600;

    // Get all existing cookies
    $cookies = $_COOKIE;

    // Iterate over the cookies and delete them
    foreach ($cookies as $cookie_name => $cookie_value) {
        // Set the cookie with an expiration time in the past
        setcookie($cookie_name, '', $expiration_time, '/');
    }
    // header("http://localhost/chatme/home.php");
    // exit;
    echo "<script type='text/javascript'> document.location ='sign_in.php'; </script>";
?>
