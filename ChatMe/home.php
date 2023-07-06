<?php 
    // error_reporting(E_ERROR | E_PARSE);
    if(isset($_COOKIE['user_id'])){
        global $id;
        global $UserName;
        global $UID;
        global $Score;
        $id = $_COOKIE['user_id'];

        $conn = new mysqli("localhost", "root", "", "chatme");

        $query = "SELECT * FROM `accounts` WHERE Mail_ID='$id'";
        
        $data = $conn->query($query);
        
        if ($data->num_rows > 0) {
            while($row = $data->fetch_assoc()) {
                if($id == $row["Mail_ID"]){
                $UserName = $row["UserName"];
                $UID = $row["UID"];
                $Score = $row["Score"];
                }
            }
        }
        else{
            // echo "<script type='text/javascript'> document.location ='sign_in.php'; </script>";
            echo "<script type='text/javascript'> alert('You opend beta version') </script>";
        }
    }
    else{
        echo "<script type='text/javascript'> document.location ='sign_up.php'; </script>";
    }
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WhatsApp Web</title>
    <!-- <link rel="stylesheet" href="css/home.css"> -->
    <link rel="stylesheet" href="css/bootstrap.css">
    <link rel="stylesheet" href="https://pro.fontawesome.com/releases/v6.0.0-beta3/css/all.css">
</head>
<body>
    <div class="header">
        <div class="contact-header">
            <div class="user-avatar">
                <a href="setting.php">
                    <img src="img/profile0.jpg" alt="Avatar">
                </a>
            </div>
            <div class="chat-info">
                <h2><?php
                        if(isset($UserName))
                            echo $UserName;
                ?></h2>
            </div>
            <a href="add_friends.php">
                <button class="activity"><i class="fa-solid fa-user-plus" style="color: #fff;"></i></button>
            </a>
        </div>
        <div class="chat-header">
            <div class="chat-avatar">
                <img src="img/profile2.jpg" alt="Avatar">
            </div>
            <h2><?php
                    if(isset($_GET["Chat_To"])){
                        echo $_GET["Chat_To"];
                    }else{
                        echo "Chat Me";

                    }
                ?></h2>
        </div>
        <div class="Bar">
            <button class="activity" onclick="menu()"><i class="fa-solid fa-bars" style="color: #ffffff;"></i></button>
        </div>
    </div>
    <div class="chat-container">
        <div class="contact-panel">
            <div class="add-friend">
                <div class="search-bar" style="width:100%;">
                    <form action="" method="post" style="width:100%;">
                        <input type="text" style="width:68%; display:inline;" list="accounts" class="mx-1 add-friend-search-box" name="search-friends-chatMe" placeholder="Add Friend" autocomplete="off"/>
                        <input type="submit" style="width:25%; display:inline;" name="add" class="btn btn-success" value="Add">
                    </form>
                    <?php
                        if(isset($_POST["add"])){
                            $query1 = "SELECT * FROM `accounts`";
                            $data = $conn->query($query1);
                            
                            $f_mail = "";
                            $f_UID = "";
                            $f_uName = "";

                            if ($data->num_rows > 0) {
                                while($row = $data->fetch_assoc()) {
                                    if($_POST["search-friends-chatMe"]==$row['UserName']){
                                        $f_mail = $row["Mail_ID"];
                                        $f_UID = $row["UID"];
                                        $f_uName = $row["UserName"];
                                    }
                                }
                            }

                            if(!$f_uName==""){
                                try{
                                    $query = "INSERT INTO `friends_$UserName`(`UID`, `UserName`, `Mail_ID`, `chatScore`) VALUES ('$f_UID','$f_uName','$f_mail',0)";
                                    $data = $conn->query($query);
                                    
                                    if($data==TRUE) {
                                        echo "<script> alert('Friend added Sucessfully') </script>";
                                    }
                                }
                                catch(Exception $e){
                                    echo "<script> alert('Friend Alrady Added') </script>";
                                }
                            }else{
                                echo "<script> alert('Wrong Data') </script>";
                            }

                        }
                    ?>
                </div>
            </div>
            
            <?php
                if(isset($UserName)){
                    $LastMessage="";
                    $query = "SELECT * FROM `friends_$UserName`";
                    
                    $data = $conn->query($query);
                    
                    if ($data->num_rows > 0) {
                        while($row = $data->fetch_assoc()) {
                            $active = "";
                            $name = $row['UserName'];

                            $LastMsgQuery = "SELECT * FROM `massges` WHERE MID=(SELECT MAX(MID) FROM `massges` WHERE (FROM_='$UserName' OR TO_='$UserName') AND (FROM_='$name' OR TO_='$name'))";
                            $message = $conn->query($LastMsgQuery);
                            global $LastMessage;
                            if($message->num_rows > 0){
                                $LastMsgRow = $message->fetch_assoc();
                                $LastMessage = $LastMsgRow['Message'];
                                $Messanger = $LastMsgRow['FROM_'];
                                if(strlen($LastMessage) > 25)
                                    $LastMessage = substr(str_replace("<br>"," ",$LastMessage),0 ,22)."...";
                                $LastMessage = $Messanger." : ".$LastMessage;
                            }else{
                                $LastMessage = "Chat Me : Start Happy Chatting.";
                            }

                            if(isset($_GET["Chat"]) && isset($_GET["Chat_To"])){
                               if($_GET["Chat_To"]==$name)
                                $active="active";
                            }

                            $Contact_Block = <<<EOT
                                <div class="chat $active">
                                    <div class="chat-avatar">
                                        <img src="img/profile1.jpg" alt="Avatar">
                                    </div>
                                    <div class="chat-info">
                                        <h2>$name</h2>
                                        <p>$LastMessage</p>
                                    </div>
                                    <div class="start-chat">
                                        <form method="GET" action="">
                                            <input type="text" style="position: absolute; left:-9999px;" name="Chat_To" value="$name">
                                            <button type="submit" style="width:5vw; display:inline;" name="Chat" class="btn btn-primary">
                                                <i class="fa-sharp fa-solid fa-paper-plane-top" style="color: #ffffff;"></i>
                                            </button>
                                        </form>
                                    </div>
                                </div>
                                EOT;
                            echo $Contact_Block;
                        }
                    }
                    else{
                        $Contact_Block = <<<EOT
                                <div class="chat active">
                                    <div class="chat-avatar">
                                        <img src="img/profile1.jpg" alt="Avatar">
                                    </div>
                                    <div class="chat-info">
                                        <h2>ChatMe</h2>
                                        <p>Happy Chatting</p>
                                    </div>
                                    <div class="start-chat">
                                        <form method="GET" action="">
                                            <input type="text" style="position: absolute; left:-9999px;" name="Chat_To" value="ChatMe">
                                            <button type="submit" style="width:5vw; display:inline;" name="Chat" class="btn btn-primary">
                                                <i class="fa-sharp fa-solid fa-paper-plane-top" style="color: #ffffff;"></i>
                                            </button>
                                        </form>
                                    </div>
                                </div>
                                EOT;
                        echo $Contact_Block;
                    }
                }
            ?>
            
        </div>
        <div class="chat-panel">
            <div class="chat-messages">
            <?php
                if(isset($_GET["Chat_To"])){
                    $Friend = $_GET["Chat_To"];
                    $MsgCollectionQuery = "SELECT * FROM `massges` WHERE (FROM_='$UserName' OR TO_='$UserName') AND (FROM_='$Friend' OR TO_='$Friend')";
                    $AllMessage = $conn->query($MsgCollectionQuery);


                    if($AllMessage->num_rows != 0){
                        while($row = $AllMessage->fetch_assoc()){
                            $message = $row['Message'];
                            $mTime = $row['Date'];
                            $sentBlock = <<< EOT
                            <div class="message sent">
                                <p>$message</p>
                                <span class="time">$mTime</span>
                            </div>
                            EOT;
                            $receivedBlock = <<< EOT
                            <div class="message received">
                                <p>$message</p>
                                <span class="time">$mTime</span>
                            </div>
                            EOT;
    
                            if($row["TO_"] === $Friend){
                                echo $sentBlock;
                            }
                            else if($row["FROM_"] === $Friend){
                                echo $receivedBlock;
                            }
                        }
                    }
                }
            ?>
            <!-- Add more message elements here -->
            </div>
            <form action="" method="post">
            <div class="chat-input">
                    <textarea placeholder="Message" name="cur-Message"></textarea>
                    <button type="submit" name="send">Send</button>
            </div>
            </form>
        </div>
    </div>
    <?php
        if(isset($_POST["send"])){
            if(isset($_GET["Chat_To"])){
                $FriendName = $_GET['Chat_To'];
                $CurMessage = $_POST['cur-Message'];
                
                // echo "<script> alert(String($curMID + '...')) </script>";
                try{
                    $InsMsgQuery = "INSERT INTO `Massges`(`FROM_`, `TO_`, `Message`, `R_To`) VALUES ('$UserName', '$FriendName', '$CurMessage', 0)";
                    $conn->query($InsMsgQuery);
                    $query = "SELECT * FROM `friends_$FriendName` WHERE UserName='$UserName'";
                    if($conn->query($query)->num_rows === 0){
                        $query = "INSERT INTO `friends_$FriendName`(`UID`, `UserName`, `Mail_ID`, `chatScore`) VALUES ('$UID','$UserName','$id',0)";
                        if(!$conn->query($query))
                            echo "<script> alert('He is not added you in their Friend List') </script>";
                    }
                }catch(Exception $e){
                    $msg = $e->getTrace();
                    echo "<script> alert('Cannot Send Message Sucessfully') </script>";
                    echo "<script> alert(String($msg)) </script>";
                }
            }
        }
    ?>
    <datalist id="accounts">
        <?php 
            $query = "SELECT * FROM `accounts`";
            $data = $conn->query($query);
            
            if ($data->num_rows > 0) {
                while($row = $data->fetch_assoc()) {
                    if($UserName!=$row['UserName'])
                    echo '<option value="'.$row['UserName'].'"> '.$row['UserName'];" </option>";
                }
            }
        ?>
    </datalist>
</body>
</html>
<style>
    * {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

img{
  width: 40px;
  height: 40px;
  border-radius: 50%;
}

body {
  font-family: Arial, sans-serif;
  background-color: #f2f2f2;
}

.contact-panel {
  width: 25%;
  background-color: #f2f2f2;
  overflow-y: scroll;
  height: 100%;
  position: relative;
  overflow-y: scroll;
}

.chat-panel {
  width: 75%;
  display: flex;
  flex-direction: column;
  background-color: #fff;
}

.chat-container {
  display: flex;
  height: calc(100vh - 7vh);
}

.chat-list {
  flex-basis: 25%;
  background-color: #fff;
  border-radius: 5px;
  overflow-y: scroll;
  padding: 10px;
}

.chat {
  display: flex;
  align-items: center;
  padding: 10px;
  border-radius: 5px;
  cursor: pointer;
  border: none;
  width: 100%;
}

.search-bar {
  display: flex;
  align-items: center;
  cursor: pointer;
}

.search-bar input[type="submit"]{
  flex-grow: 1;
  padding: 5px;
  border-radius: 5px;
  border: none;
  resize: none;
  width: 20%;
  align-self: flex-end;
}

.search-bar input[type="text"]{
  flex-grow: 1;
  padding: 5px;
  border-radius: 5px;
  border: none;
  width: 80%;
  resize: none;
  align-self: flex-start;
}

.chat .active {
  background-color: #000;
  color: #fff;
}

.chat-avatar img {
  margin-right: 10px;
}

.start-chat {
  margin-left: 10px;
  align-items: flex-end;
}

.chat-window {
  flex-grow: 1;
  margin-left: 20px;
  background-color: #fff;
  border-radius: 5px;
  overflow-y: scroll;
}

.contact-header {
  display: flex;
  align-items: center;
  padding: 10px;
  width: 25%;
  border-bottom: 1px solid #ccc;
  height: 7vh;
}
.header{
  display: flex;
  background-color: rgb(255, 132, 0);
  color: #fff;
}

.activity{
  font-weight: bolder;
  font-size: x-large;
  background-color: #fff0;
  border: none;
  margin-left: 30px;
}

.chat-header {
  display: flex;
  align-items: center;
  padding: 10px;
  width: calc(100% - 25%);
  border-bottom: 1px solid #ccc;
  height: 7vh;
}


.Bar{
  display: none;
}

.contact-header img {
  margin-right: 10px;
  align-self: flex-start;
}

.chat-info {
  flex-grow: 1;
}

.chat-info h2{
  font-size: x-large;
}

.user-avatar img {
  margin-right: 10px;
}

.chat-messages {
  padding: 10px;
  height: 90%;
  overflow-y: scroll;
}

.message {
  display: flex;
  flex-direction: column;
  margin-bottom: 10px;
}

.message p {
  padding: 10px;
  border-radius: 10px;
  max-width: 70%;
  word-wrap: break-word;
}

.message.received p {
  background-color: #ebebeb;
  align-self: flex-start;
}

.message.sent p {
  background-color: #dcf8c6;
  align-self: flex-end;
}

.message.sent .time {
  font-size: 12px;
  color: #888;
  align-self: flex-end;
  margin-top: 5px;
}

.message.received .time {
  font-size: 12px;
  color: #888;
  align-self: flex-start;
  margin-top: 5px;
}


/* Additional styling to match web.whatsapp.com */
.container,
.contact-panel,
.chat-panel {
  box-sizing: border-box;
}

.contact-panel::-webkit-scrollbar {
  width: 8px;
}

.contact-panel::-webkit-scrollbar-thumb {
  background-color: rgba(0, 0, 0, 0.2);
  border-radius: 4px;
}

.contact-panel::-webkit-scrollbar-thumb:hover {
  background-color: rgba(0, 0, 0, 0.4);
}

.chat-messages:-webkit-scrollbar {
  width: 8px;
}

.chat-messages::-webkit-scrollbar-thumb {
  background-color: rgba(0, 0, 0, 0.2);
  border-radius: 4px;
}

.chat-messages::-webkit-scrollbar-thumb:hover {
  background-color: rgba(0, 0, 0, 0.4);
}

.chat-messages::-webkit-scrollbar-track {
  background-color: transparent;
}

.chat-input {
  display: flex;
  align-items: center;
  padding: 10px;
  border-top: 1px solid #ccc;
  position: fixed;
  bottom: 0px;
  height: 10%;
  width: 75%;
}

.chat-input textarea {
  flex-grow: 1;
  padding: 5px;
  border-radius: 5px;
  border: none;
  border-radius: 5px;
  /* background-color: #fff; */
  resize: none;
}

.chat-input textarea:focus {
  outline: none;
  background-color: #fff;
}

.chat-input textarea~label {
  position: absolute;
  top: 10px;
  left: 10px;
  font-size: 12px;
  color: #888;
  transition: all 0.2s ease;
  pointer-events: none;
}

.chat-input textarea:focus~label,
.chat-input textarea:not(:placeholder-shown)~label {
  transform: translateY(-15px);
  font-size: 10px;
  color: #555;
}

.fa-paper-plane-top{
    font-size:1.75vw;
}

.chat-input button {
  padding: 5px 10px;
  border-radius: 5px;
  background-color: #4caf50;
  color: #fff;
  border: none;
  margin-left: 10px;
  cursor: pointer;
}

/* Media Queries for Responsiveness */

@media screen and (max-width: 600px) {
  .chat-container {
    flex-direction: column;
  }

  .chat-list,
  .chat-window {
    margin: 0;
    margin-top: 20px;
  }
}

.add-friend{
  display: flex;
  align-items: center;
  padding: 10px;
  border-radius: 5px;
  width: 100%;
}


/* Media query for medium-sized screens */
@media screen and (max-width: 1350px) {
  .contact-panel, .contact-header {
    width: 30%;
  }
  .chat-panel, .chat-header{
    width: 70%;
  }
  .search-bar input[type="text"]{
    width: 20vw;
  }
}

@media screen and (max-width: 1080px) {
  .activity{
    margin-left: 00px;
  }
  
    .fa-paper-plane-top{
        font-size:medium;
    }
  
}
@media screen and (max-width: 945px) {
  .contact-panel, .contact-header {
    width: 35%;
  }
  .chat-panel, .chat-header{
    width: 65%;
  }
}
@media screen and (max-width: 656px) {
  .Bar{
    display: block;
    margin: auto;
    margin-right: 5%;
    cursor:pointer;
  }
  .contact-panel, .contact-header {
    display: none;
    width: 100vw;
  }
  .chat-header{
    width: 95vh;
  }
  .chat-input,.chat-panel,.contact-panel{
    width: 100vw;
  }
  .chat-header, .chat-input,.contact-header{
    height: 10vh;
  }
  .chat-panel, .contact-panel {
    height: 90vh;
  }
  .activity,.user-avatar{
    width: 15%;
  }
  .contact-header{
    width: 70%;
  }
}
.user-name{
  display: inline;
  flex-grow: 1;
  align-self: flex-end;
}

.btn{
  display: inline;
}
</style>