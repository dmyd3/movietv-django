
$(document).ready(function () {

    $("#btnWatchMovie").change( function() {

        let film_json = JSON.parse(document.getElementById('film_json').textContent);
        year = new Date(film_json['release_date']).getFullYear();
        new_film_json = {
            'original_title': film_json['original_title'],
            'release_year': year,
            'runtime': film_json['runtime'],
            'id': film_json['id']
        }
        json_string = JSON.stringify(new_film_json)
        
        let form = $("#movie_data").serialize()
        let form_film = form + "&data=" + json_string

        if( $(this).is(":checked") ){
            console.log("WATCH CHECKED")
            form_film = form_film + "&check=True"

            $.ajax({
                type:'POST',
                url: '/ajax/watch_movie',
                data: form_film,
                success: function () {
                    $("#btnWatchMovie").next().children().toggleClass('bi-eye bi-eye-fill');
                }
            })
        }else{
            console.log("WATCH NOT CHECKED")
            form_film = form_film + "&check=False"

            $.ajax({
                type:'POST',
                url: '/ajax/watch_movie',
                data: form_film,
                success: function () {
                    $("#btnWatchMovie").next().children().toggleClass('bi-eye bi-eye-fill');
                }
            })
        }
    });
    
    $("#btnFavMovie").change( function() {
        
        let film_json = JSON.parse(document.getElementById('film_json').textContent);
        year = new Date(film_json['release_date']).getFullYear();
        new_film_json = {
            'original_title': film_json['original_title'],
            'release_year': year,
            'runtime': film_json['runtime'],
            'id': film_json['id']
        }
        json_string = JSON.stringify(new_film_json)
        
        let form = $("#movie_data").serialize()
        let form_film = form + "&data=" + json_string

        if( $(this).is(":checked") ){
            console.log("FAV CHECKED")
            form_film = form_film + "&check=True"

            $.ajax({
                type:'POST',
                url: '/ajax/fav_movie',
                data: form_film,
                success: function () {
                    $("#btnFavMovie").next().children().toggleClass('bi-heart bi-heart-fill');
                }
            })
        }else{
            console.log("FAV NOT CHECKED")
            form_film = form_film + "&check=False"

            $.ajax({
                type:'POST',
                url: '/ajax/fav_movie',
                data: form_film,
                success: function () {
                    $("#btnFavMovie").next().children().toggleClass('bi-heart bi-heart-fill');
                }
            })
        }

    });

});
