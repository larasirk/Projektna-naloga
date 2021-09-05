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
        <div class="row trgatev">
            <div>
                <h1>Trgatev</h1>
                <form action="/posodobi_trgatev" method="post">
                    <input type="hidden" name="st_trgatve" value="{{trgatev.st_trgatve}}">
                    <div>
                        <label for="kolicina">Količina</label>
                        <input type="text" name="kolicina" value="{{trgatev.kolicina}}" pattern="^[0-9]+$"
                            required="required">
                        <label>kg</label>
                    </div>

                    <div>
                        <label for="datum">Datum</label>
                        <input type="date" name="datum" required="required"
                            value="{{trgatev.datum.strftime('%Y-%m-%d')}}">
                    </div>
                    <div>
                        <label for="st_sorte">Sorta</label>
                        <select name="st_sorte">
                            % for sorta in sorte:
                            <option value="{{sorta.st_sorte}}"
                                % if trgatev.sorta.st_sorte==sorta.st_sorte: 
                                    selected="selected" 
                                % end
                                >
                                {{sorta.ime}}
                            </option>
                            % end
                        </select>
                    </div>
                    <ul>
                        <li>Sok: {{"{:.2f}".format(trgatev.sok)}} l</li>
                        <li>Taille: {{"{:.2f}".format(trgatev.taille)}} l</li>
                        <li>Cuvee: {{"{:.2f}".format(trgatev.cuvee)}} l</li>
                        <li>Kislina cuvee: {{"{:.2f}".format(trgatev.kislina_cuvee)}} kg</li>
                        <li>Encimi cuvee: {{"{:.2f}".format(trgatev.encimi_cuvee)}} kg</li>
                        <li>Čistilo cuvee: {{"{:.2f}".format(trgatev.cistilo_cuvee)}} l</li>
                        <li>Kislina taille: {{"{:.2f}".format(trgatev.kislina_taille)}} kg</li>
                        <li>Encimi taille: {{"{:.2f}".format(trgatev.encimi_taille)}} kg</li>
                        <li>Čistilo taille: {{"{:.2f}".format(trgatev.cistilo_taille)}} l</li>
                        <li>Carbon taille: {{"{:.2f}".format(trgatev.carbon_taille)}} kg</li>
                        <li>Ime čistila taille: {{trgatev.sorta.cistilo_ime_taille}}</li>
                        <li>Ime čistila cuvee: {{trgatev.sorta.cistilo_ime_cuvee}}</li>
                    </ul>

                    <button class="black-button" type="submit">Posodobi</button>
                    <a href="/">
                        <div class="button red-button">Nazaj</div>
                    </a>
                </form>
            </div>
        </div>
    </div>
</body>

</html>