<!DOCTYPE html>
<html>
<head>
    <title>Browser Information</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            padding: 20px;
        }
        .info-box {
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
            max-width: 500px;
        }
        h2 {
            text-align: center;
        }
        p {
            margin: 8px 0;
        }
    </style>
</head>
<body>

<div class="info-box">
    <h2>Browser Information</h2>
    <p><strong>Browser Name:</strong> <span id="browserName"></span></p>
    <p><strong>Browser Version:</strong> <span id="browserVersion"></span></p>
    <p><strong>Platform:</strong> <span id="platform"></span></p>
    <p><strong>User Agent:</strong> <span id="userAgent"></span></p>
    <p><strong>Cookies Enabled:</strong> <span id="cookies"></span></p>
    <p><strong>Online Status:</strong> <span id="onlineStatus"></span></p>
    <p><strong>Screen Resolution:</strong> <span id="resolution"></span></p>
</div>

<script>
    function getBrowserInfo() {
        document.getElementById("browserName").innerText = navigator.appName;
        document.getElementById("browserVersion").innerText = navigator.appVersion;
        document.getElementById("platform").innerText = navigator.platform;
        document.getElementById("userAgent").innerText = navigator.userAgent;
        document.getElementById("cookies").innerText = navigator.cookieEnabled ? "Yes" : "No";
        document.getElementById("onlineStatus").innerText = navigator.onLine ? "Online" : "Offline";
        document.getElementById("resolution").innerText = screen.width + " x " + screen.height;
    }

    getBrowserInfo();
</script>

</body>
</html>
