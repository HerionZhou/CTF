<?php
include "config.php";
$id =$_GET["id"];
$host = $_GET["host"];
$pass=$_GET["pass"];
if(isset($pass)){
	if(strtolower($pass)!=strtolower(md5("1234asdfgeawrbaewgwbweEEFAEFbaaaa"))){
		die("error");
	}
}else{
	die("error");
}
if(empty($host)) die("error");
if(strpos($host,"..")>-1) die("error");
if(empty($id)) die("error");
if(strpos($id,"..")>-1) die("error");
if($host!="proxy") die("error");

$path = $ROOT_SAVE_PATH."/".$host."/".$id;//好吧我承认，这个密码并没有卵用……
if(file_exists($path)){
	header("Cache-Control: public"); 
	header("Content-Description: File Transfer"); 
	header('Content-disposition: attachment; filename='.basename($path)); //文件名   
	header("Content-Transfer-Encoding: binary"); //告诉浏览器，这是二进制文件    
	header('Content-Length: '. filesize($path)); //告诉浏览器，文件大小   
	@readfile($path);
	@unlink($path);
}else{
	header('HTTP/1.1 404 Not Found');
    header("status: 404 Not Found");
}
?>