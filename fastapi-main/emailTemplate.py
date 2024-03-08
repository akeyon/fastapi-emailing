# Email template
import base64


    
email_template = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Email Template</title>
<style>
    body {
        font-family: Arial, sans-serif;
        line-height: 1.6;
        margin: 0;
        padding: 0;
        background-color: #f4f4f4;
    }

    .container {
        max-width: 600px;
        margin: 20px auto;
        padding: 20px;
        background-color: #fff;
        border-radius: 5px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }

    h1 {
        color: #333;
        text-align: center;
    }

    p {
        color: #555;
        margin-bottom: 20px;
    }

    .btn {
        display: inline-block;
        padding: 10px 20px;
        background-color: #007bff;
        color: #fff;
        text-decoration: none;
        border-radius: 3px;
    }

    .btn:hover {
        background-color: #0056b3;
    }

    .banner {
        width: 100%;
        max-height: 200px;
        object-fit: cover;
        border-radius: 5px;
    }

    @media only screen and (max-width: 600px) {
        .container {
            padding: 10px;
        }

        h1 {
            font-size: 24px;
        }

        p {
            font-size: 14px;
        }

        .btn {
            padding: 8px 16px;
        }

        .banner {
            max-height: 150px;
        }
    }
</style>
</head>
<body>
    <div class="container">
    
     
        
        <p>Dear [Participant's Name],</p>
        <p>We hope this message finds you well. </p>
        <p>Marathon XP, a service design firm, (https://www.marathonxp.com/)  is thrilled to announce our partnership with Tuwatunze, a learning support center for children with learning disabilities, in an impactful Corporate Social Responsibility (CSR) project.</p>
        <p>Our initiative is designed to bridge the gap between parental expectations and children's education, while concurrently raising awareness about special education for children grappling with learning disabilities. </p>
        <p>In pursuit of these objectives, Marathon XP is hosting an open day with a workshop experience on <b>13th April 2024 at Playstreet Lavington, Mugumo road from 9am to 2pm</b>. The event will include a panel discussion featuring experts in the field of learning disabilities in children and educators</p>
        <p>We can’t wait to meet you! </p>
        <p>See you soon! </p>

    </div>
</body>
</html>

"""