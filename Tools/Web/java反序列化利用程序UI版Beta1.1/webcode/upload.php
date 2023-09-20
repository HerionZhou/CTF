<?php
include "config.php";
function create_path_if_not_ext($path){
	if(!is_dir($path)){
		$res=mkdir($path,0755,true);
	}
}
if(is_uploaded_file($_FILES["uploadfile"]["tmp_name"])){
	$upfile=$_FILES["uploadfile"];
	$name=$upfile["name"];
	$type=$upfile["type"];
	$size=$upfile["size"];
	$tmp_name=$upfile["tmp_name"];
	$error=$upfile["error"];
	$id = $_GET["id"];
	$host = $_GET["host"];
	$path = str_replace("..","",$path);
	$name = str_replace("..","",$name);
	$host = str_replace("..","",$host);

	$path = $ROOT_SAVE_PATH.'/'.$host;
	create_path_if_not_ext($path);
	if($error=='0'){
		move_uploaded_file($tmp_name,$path.'/'.$id.'_'.$name);
		echo "ok";
	}else{
		echo "error";
	}
}
?>