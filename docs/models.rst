API Models
==========

.. currentmodule:: kitsu

Anime
-----

.. autoclass:: Anime()
    :members:


.. autoclass:: Episode()
    :members:

Manga
-----

.. autoclass:: Manga()
    :members:

Enumerations
------------

.. class:: AgeRating
    :canonical: kitsu.enums.AgeRating

    Denotes the age rating of a Media.

    .. attribute:: G

        Rated for general audiences.
    
    .. attribute:: PG

        Rated as parental guidance suggested.
    
    .. attribute:: R

        Rated as restricted.
    
    .. attribute:: R18

        Rated as explicit.


.. class:: Status
    :canonical: kitsu.enums.Status

    Denotes the status of an Anime or Manga.

    .. attribute:: current

        The media is currently releasing.
    
    .. attribute:: finished

        The media has finished releasing.
    
    .. attribute:: tba

        The media is tba (to be announced).
    
    .. attribute:: unreleased

        The media is unreleased.
    
    .. attribute:: upcoming

        The media is upcoming.

.. class:: Season
    :canonical: kitsu.enums.Season

    Denotes the release season of an Anime or Manga.

    .. attribute:: spring

        The media was released/will release in spring.

    .. attribute:: summer

        The media was released/will release in summer.
    
    .. attribute:: fall

        The media was released/will release in fall.
    
    .. attribute:: winter

        The media was released/will release in winter.

.. class:: AnimeSubtype
    :canonical: kitsu.enums.AnimeSubtype

    Denotes the subtype of an Anime.

    .. attribute:: ONA

        The anime is an ONA (Original Net Animation).
    
    .. attribute:: OVA

        The anime is an OVA (Original Video Animation).
    
    .. attribute:: TV

        The anime is a TV series.

    .. attribute:: movie

        The anime is a movie.
    
    .. attribute:: music

        The anime is a music.
    
    .. attribute:: special

        The anime is a special.

.. class:: MangaSubtype
    :canonical: kitsu.enums.MangaSubtype

    Denotes the subtype of a Manga.

    .. attribute:: doujin
    
    .. attribute:: manga

    .. attribute:: manhua
    
    .. attribute:: manwha
    
    .. attribute:: novel

    .. attribute:: oel
    
    .. attribute:: oneshot
