function PressKeyAndWait(buttonid, timeout) {
                var button = document.getElementById(buttonid);
                button.click();
                setTimeout(window.stop(), timeout) 
        }