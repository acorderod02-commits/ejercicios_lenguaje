<?php 
if(isset($_POST['email'])) { 
 
$email_to = "tu_dirección@educarex.es"; 
$email_subject = "Contacto desde el sitio web"; 
 
if(empty($_POST['nombre']) || 
empty($_POST['apellidos']) || 
empty($_POST['email']) || 
empty($_POST['telefono']) || 
empty($_POST['comentarios'])) { 
 
echo "<b>Ocurri&oacute un error y el formulario no ha sido enviado. </b><br />"; 
echo "Por favor, vuelva atr&aacutes y verifique la informaci&oacuten introducida<br />"; 
die(); 
} 
$email_message = "Detalles del formulario de contacto:\n\n"; 
$email_message .= "Nombre: " . $_POST['nombre'] . "\n"; 
$email_message .= "Apellidos: " . $_POST['apellidos'] . "\n"; 
$email_message .= "E-mail: " . $_POST['email'] . "\n"; 
$email_message .= "Teléfono: " . $_POST['telefono'] . "\n"; 
$email_message .= "Comentarios: " . $_POST['comentarios'] . "\n\n"; 
 
$headers = 'From: '.$email_from."\r\n". 
'Reply-To: '.$email_from."\r\n" . 
'X-Mailer: PHP/' . phpversion(); 
@mail($email_to, $email_subject, $email_message, $headers); 
 
echo "El formulario ha sido enviado"; 
} 
?> 