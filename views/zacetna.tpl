<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8"> 
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="/static/css/style.css">
    <link rel="icon" type="image/png" href="/static/img/ikona.png"/>

    <title>Trgatve</title>
</head>

<body>
    <div class="container">
        <div class="row">
            <div class="column">
                <h1>Vnesi trgatev</h1>
                <form action="/dodaj_trgatev" method="post">
                    <div>
                        <label for="kolicina">Količina</label>
                        <input type="text" name="kolicina" placeholder="vnesi količino v kg" pattern="^[0-9]+$"
                            required="required">
                    </div>

                    <div>
                        <label for="st_sorte">Sorta</label>
                        <select name="st_sorte">
                            % for sorta in sorte: 
                            <option value="{{sorta.st_sorte}}">
                                {{sorta.ime}}
                            </option>
                            % end 
                        </select>
                    </div>

                    <div>
                        <label for="datum">Datum trgatve</label>
                        <input type="date" name="datum" required="required">
                    </div>

                    <div class="button-container">
                        <button class="black-button" type="submit">Dodaj</button>
                    </div>
                </form>
            </div>
        </div>

    % if trgatve: 
        <div class="row">
            <div class="column">
                <h1>Shranjene trgatve</h1>
                <div class="container-trgatev">

                    % for trgatev in trgatve:
                    <div class="trgatev-item">
                        <h3>{{trgatev.datum.strftime('%Y-%m-%d')}}</h3>
                        <ul>
                            <li>Sorta: {{trgatev.sorta.ime}} </li>
                            <li>Količina: {{trgatev.kolicina}} kg</li>
                            <li>Sok: {{"{:.2f}".format(trgatev.sok)}} l</li>
                            <li>Taille: {{"{:.2f}".format(trgatev.taille)}} l</li>
                            <li>Cuvee: {{"{:.2f}".format(trgatev.cuvee)}} l</li>
                        </ul>

                        <a href="/trgatev/{{trgatev.st_trgatve}}">
                            <div class="button black-button">Prikaži več
                            </div>
                        </a>
                        <a href="/izbrisi_trgatev/{{trgatev.st_trgatve}}">
                            <div class="button red-button">Izbriši</div>
                        </a>

                    </div>
                    % end
                </div>
            </div>
        </div>
    % end 
        <div class="row">

            <div class="column">
                <h1>Skupna količina grozdja in soka posamezne sorte</h1>
                <div class="bottom">
                    % for sorta in sorte: 
                    <div>
                        <h3>
                            {{sorta.ime}}
                        </h3>
                        <ul>
                            <li>Količina: {{kolicina[sorta.st_sorte]}} kg</li>
                            <li>Sok: {{sok[sorta.st_sorte]}} l</li>
                        </ul>
                    </div>
                    % end
                </div>
            </div>
        </div>
    </div>


    </div>
</body>

</html>