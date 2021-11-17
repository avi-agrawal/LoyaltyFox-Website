<!DOCTYPE html>
<html lang="en">
<head>
    <!-- Required meta tags -->
    <title>loyalty</title> 
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
	
    <!-- CSS Links-->
    <link rel="icon" href="img/favicon.ico">
	<link href="https://fonts.googleapis.com/css?family=Montserrat:300,400,500,600,700,800,900&display=swap" rel="stylesheet">
	<link rel="stylesheet" href="css/bootstrap.min.css">
    <link rel="stylesheet" href="css/custum.css">


    <!-- Global site tag (gtag.js) - Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=UA-147737631-1"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());

      gtag('config', 'UA-147737631-1');
    </script>

    <!-- Global site tag (gtag.js) - Google Ads: 709476094 -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=AW-709476094"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());

      gtag('config', 'AW-709476094');
    </script>

    <!-- Event snippet for Lead From PPC conversion page -->
    <script>
      gtag('event', 'conversion', {'send_to': 'AW-709476094/rKM5COXxoqwBEP79ptIC'});
    </script>


    <!-- Facebook Pixel Code -->
    <script>
      !function(f,b,e,v,n,t,s)
      {if(f.fbq)return;n=f.fbq=function(){n.callMethod?
      n.callMethod.apply(n,arguments):n.queue.push(arguments)};
      if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
      n.queue=[];t=b.createElement(e);t.async=!0;
      t.src=v;s=b.getElementsByTagName(e)[0];
      s.parentNode.insertBefore(t,s)}(window, document,'script',
      'https://connect.facebook.net/en_US/fbevents.js');
      fbq('init', '547431919153961');
      fbq('track', 'PageView');
    </script>
    <noscript><img height="1" width="1" style="display:none"
      src="https://www.facebook.com/tr?id=547431919153961&ev=PageView&noscript=1"
    /></noscript>
    <!-- End Facebook Pixel Code -->


</head>

<?php

if(isset($_POST['submit'])):

	date_default_timezone_set('Asia/Kolkata');

	$name 	= filter_var($_POST['name'], 	FILTER_SANITIZE_STRING);
	$email 	= filter_var($_POST['email'], 	FILTER_SANITIZE_EMAIL);
	$phone 	= filter_var($_POST['phone'], 	FILTER_SANITIZE_NUMBER_INT);
	//$company= filter_var($_POST['company'], FILTER_SANITIZE_STRING);
	//$city 	= filter_var($_POST['city'], 	FILTER_SANITIZE_STRING);
	$message= filter_var($_POST['message'], FILTER_SANITIZE_STRING);

	$source = "Loyalty";
	$date 	= date('Y-m-d H:i:s');


		//if( !empty($name) && !empty($email) && !empty($phone) && !empty($message) && !empty($company) && !empty($city) ):
		if( !empty($name) && !empty($email) && !empty($phone) && !empty($message) ):

					$email_message .= "Name: 	"   . $name   . "<br/>";
                    $email_message .= "Phone No:"  	. $phone  . "<br/>";
                    $email_message .= "Email: 	"   . $email  . "<br/>";
                    //$email_message .= "Company: "   . $company. "<br/>";
                    //$email_message .= "City: 	"   . $city   . "<br/>";
                    $email_message .= "Message: "   . $message. "<br/>";
                    
                    $to             = "info@loyaltyfox.com, awadheshp@elixirweb.us, ishita@loyaltyfox.com, shoaib@loyaltyfox.com";
                    #$to             = "pavank@elixirweb.us";




                    $subject        = "Enquiry for Loyalty Program";
                    
                    $headers        = 'MIME-Version: 1.0'                           	 . "\r\n";
                    $headers       .= 'Content-type: text/html; charset=iso-8859-1' 	 . "\r\n";
                    $headers       .= 'From: <info@loyaltyfox.com>'			 	 		 . "\r\n";
         
                    
                    if ( ! mail( $to, $subject, $email_message, $headers ) ):
                    	header('location:index.html?mail_not_sent'); exit;
                    endif;

		else:
			header('location:index.html?empty_fields');
		endif;


else:
	header('location:index.html');
endif;
?>

<body class="thanku_bg">
	<div class="outer-container">
		<!-- head-section-->
		<header class="header">
			<div class="container clearfix">
				<div class="logo">
					<a href="#"><img src="img/logo.png" alt="logo"></a>
				</div>
				<div class="head-phone botm_btn">
					<a href="tel:+918287540278"><img src="img/call.png"> <span class="hidden-mob">8287540278 | 011-45645872</span></a>
					<a href="mailto:info@loyaltyfox.com" class="hidden-mob"><img src="img/email.png"> <span>info@loyaltyfox.com</span></a>
					<a href="#top_formm" class="contct-btn show-mob">Contact Us</a>
				</div>
			</div>
		</header>
		
		<div class="thank">
			<div class="maimm">
				<h1>THANK YOU</h1>
				<p>We will contact You Soon</p>
			</div>
		</div>
	</div>
</body>
</html>