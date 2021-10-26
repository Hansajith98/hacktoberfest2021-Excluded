<?php

$mtk = 65;
$inggris = 80;
$indonesia = 82;

// cara penulisan pertama
if ($mtk >= 70 && $inggris >= 75 && $indonesia >= 75) {
  echo "Anda mendapat nilai A" . PHP_EOL;
} else if ($mtk >= 60 && $inggris >= 70 && $indonesia >= 70) {
  echo "Anda mendapat nilai B" . PHP_EOL;
} else if ($mtk >= 55 && $inggris >= 60 && $indonesia >= 60) {
  echo "Anda mendapat nilai C" . PHP_EOL;
} else {
  echo "Anda mendapat nilai D" . PHP_EOL;
}

// cara penulisan kedua / syntax alternatif
if ($mtk >= 70 && $inggris >= 75 && $indonesia >= 75) :
  echo "Anda mendapat nilai A" . PHP_EOL;
elseif ($mtk >= 60 && $inggris >= 70 && $indonesia >= 70) :
  echo "Anda mendapat nilai B" . PHP_EOL;
elseif ($mtk >= 55 && $inggris >= 60 && $indonesia >= 60) :
  echo "Anda mendapat nilai C" . PHP_EOL;
else :
  echo "Anda mendapat nilai D" . PHP_EOL;
endif;
