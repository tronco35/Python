

import requests
from bs4 import BeautifulSoup ## es una libreria de web scraping


url = "https://www.linkedin.com/jobs/search/?geoId=100876405&keywords=SQL&location=Colombia"# solo ofertas que sean superiores a 100 con el valor

if "__main__" == __name__:
        page = requests.get(url)
        soup = BeautifulSoup (page.content, "html.parser") #contenido que se debe parsear

        def has_data_search(tag): #definimos la funcion que va buscar las etiquetas
            return tag.has_attr("ember738") #busca cada atributo data-search-sol-meta

        results = soup.find_all(has_data_search) # llama el metodo find_all del html ya parseado
        for job in results:
                try:
                    titleElement = job.find("a", attrs={"data-automation": "jobTitle"})
                    title = titleElement.get_text()
                    company = job.find("a", attrs={"data-automation": "jobCompany"}).get_text()
                    joblink = "www.linkedin.com" + titleElement['href']# retorna el lnk de la oferta laboral
                    salary = job.find("span", attrs={"data-automation": "jobSalary"})
                    salary = salary.get_text() if salary else 'n/a'# si el salario existe lo asigna si no retorna N/A

                    job = "Titulo: {}\nempresa: {}\nSalario: {}\nLink: {}\n"# contruir instring con los vaiables

                    job = job.format(title, company, salary, joblink)# imprimir en terminal
                    print (job ) 

                except Exception as e:
                    print("Exception: {}".format(e))
                    pass
