<?php
$x = 1;

while($x <= 5) {
  echo "The number is: $x <br>";
  $x++;
}

$y = 1;

do {
  echo "The number is: $y <br>";
  $y++;
} while ($y <= 5);


for ($z = 0; $z <= 10; $z++) {
  echo "The number is: $z <br>";
}

$names= array("rob", "boby", "micky", "roke");

foreach $names= as $value) {
  echo "$value <br>";
}

?>