<?php
$insert = false;
if(isset($_POST['date'])){
    // Set connection variables
    $server = "localhost";
    $username = "root";
    $password = "";

    // Create a database connection
    $con = mysqli_connect($server, $username, $password);

    // Check for connection success
    if(!$con){
        die("connection to this database failed due to" . mysqli_connect_error());
    }
    // echo "Success connecting to the db";

    // Collect post variables
    $date=$_POST['date'];
    $time=$_POST['time'];
    $task=$_POST['task'];
    $note=$_POST['note'];
    $sql = "INSERT INTO `task`.`task` (`date`, `time`, `task`, `note`, `dateofentry`) VALUES ('$date', '$time', '$task', '$note', current_timestamp());";
    // echo $sql;

    // Execute the query
    if($con->query($sql) == true){
        // echo "Successfully inserted";

        // Flag for successful insertion
        $insert = true;
    }
    else{
        echo "ERROR: $sql <br> $con->error";
    }

    // Close the database connection
    $con->close();
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width,initial-scale=1.0">
    <title>Welcome to To-Do List form</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Climate+Crisis&family=Mynerve&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <img class="bg" src="bg.jpg" alt="Assignment2">
    <div class="container">
        <h1>TO DO list</h3>
        <p>Entry on the to do list</p>
        <?php
        if($insert==true){
        echo "<p class='SubmitMsg'>Thanks for filling the form. We will add your list to the calender.</p>";
        }
        ?>
        <form action="index.php" method="post">
            <input type="date" name="date" id="date" placeholder="Enter the date">
            <input type="time" name="time" id="time" placeholder="Enter the time">
            <input type="text" name="task" id="task" placeholder="Enter the task">
            <textarea name="note" id="note" cols="30" rows="10" placeholder="Enter any notes here"></textarea>        
            <button class="btn">Submit</button>
    </div>
    <script src="index.js"></script>
</body>
</html>