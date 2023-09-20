<?php
include "config.php";
function create_path_if_not_ext($path){
	if(!is_dir($path)){
		$res=mkdir($path,0755,true);
	}
}
$value = $_POST["value"];
$host = $_REQUEST["host"];
$id = $_REQUEST["id"];

if(empty($host)) die("error");
if(strpos($host,"..")>-1) die("error");
if(empty($id)) die("error");
if(strpos($id,"..")>-1) die("error");

if(!empty($value)){
	create_path_if_not_ext($ROOT_SAVE_PATH.'/'.$host);
	$list = json_decode($value);
	var_dump($list);
	$fp=fopen($ROOT_SAVE_PATH.'/'.$host."/".$id,"w");
	fwrite($fp,$value);
	fclose($fp);
}
?>