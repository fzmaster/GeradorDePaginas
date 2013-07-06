"""
This code generates files automatically
"""

minimo = 1;
maximo = 300;
for i in range(minimo,maximo):
    nomeArquivo = "id-"+str(i)+".html";
    file = open(nomeArquivo, 'w');
    file.write('<html><head><script type="text/javascript"><!-- \n function delayer(){    window.location = "https://www.facebook.com/<REDIRECIONADOR>"}//--></script></head><body onLoad="setTimeout(\'delayer()\', 50)"><h2>Redirecionando...</h2><p>Aguarde....</p></body></html>');
    file.close();
