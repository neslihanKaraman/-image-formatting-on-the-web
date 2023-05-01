<?php
    if(isset($_POST["submit"])) {

      $file = $_FILES["fileToUpload"];
      $target_dir = "uploads/";
      $edited_image_path = 'uploads/edited.jpg';
      move_uploaded_file($file["tmp_name"], $edited_image_path);


      $width = $_POST["width"];
      $height = $_POST["height"];
      $angle = $_POST["angle"];
      $flip = $_POST["flip"];
      $crop_top = $_POST["crop_top"];
      $crop_bottom = $_POST["crop_bottom"];
      $crop_left = $_POST["crop_left"];
      $crop_right = $_POST["crop_right"];
    }


#py dosyasına veri aktarmak için
$python_command = "python3 bicimlendir.py "
            . escapeshellarg($width) . " "
            . escapeshellarg($height) . " "
            . escapeshellarg($angle) . " "
            . escapeshellarg($flip) . " "
            . escapeshellarg($crop_top) . " "
            . escapeshellarg($crop_bottom) . " "
            . escapeshellarg($crop_left) . " "
            . escapeshellarg($crop_right)." "
            . escapeshellarg($edited_image_path);

$output = shell_exec($python_command);

$edited_image = file_get_contents($edited_image_path);

// düzenlenmiş resmi base64 ile kodla
$edited_image_base64 = base64_encode($edited_image);

echo '<img src="data:image/png;base64,' . $edited_image_base64 . '">';

?>
