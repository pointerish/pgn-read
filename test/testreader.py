# testreader.py
# Copyright 2010 Roger Marsh
# Licence: See LICENCE (BSD licence)

"""Test Portable Game Notation (PGN) reader."""


if __name__ == '__main__':

    import datetime
    import cStringIO

    from pgn.core.reader import PGNReader

    pgndata = '\n'.join((
        '[Event "4NCL-9899A BA1-BA2"]',
        '[Site "Rd1-Warwick"]',
        '[Date "1998.10.24"]',
        '[Round "1.1"]',
        '[White "Kopec, Danny"]',
        '[Black "Crouch, Colin"]',
        '[Result "1/2-1/2"]',
        '[ECO "B02"]',
        '[WhiteElo "2400"]',
        '[BlackElo "2410"]',
        '[PlyCount "67"]',
        '[EventDate "1998.10.24"]',
        '',
        '1. e4 Nf6 2. e5 Nd5 3. Nc3 Nxc3 4. dxc3 Nc6 5. Nf3 d6 6. Bb5 e6 7. Bf4 Be7 8.',
        'Qe2 a6 9. Bxc6+ bxc6 10. Rd1 d5 11. h4 Bd7 12. Bg5 O-O 13. Rd4 f5 14. exf6 gxf6',
        '15. Bh6 Rf7 16. Rg4+ Kh8 17. Rf4 Be8 18. Qxe6 Bd6 19. Rg4 Qe7 20. Qxe7 Rxe7+',
        '21. Kd2 Bd7 22. Ra4 c5 23. Ra5 Bb5 24. a4 Bd7 25. Re1 Rxe1 26. Nxe1 c6 27. Nd3',
        'Bc7 28. Rxc5 Bb6 29. Be3 Bxc5 30. Nxc5 Bc8 31. a5 Kg7 32. g3 Kf7 33. Bf4 Bg4',
        '34. b4 1/2-1/2',
        '',
        '[Event "4NCL-9899A BA1-BA2"]',
        '[Site "Rd1-Warwick"]',
        '[Date "1998.10.24"]',
        '[Round "1.2"]',
        '[White "Lewis, Andrew P"]',
        '[Black "Rogers, Jonathan"]',
        '[Result "1/2-1/2"]',
        '[ECO "A10"]',
        '[WhiteElo "2275"]',
        '[BlackElo "2355"]',
        '[PlyCount "74"]',
        '[EventDate "1998.10.24"]',
        '',
        '1. c4 e6 2. Nf3 f5 3. g3 Nf6 4. Bg2 Be7 5. O-O O-O 6. b3 $4 Ne4 7. Bb2 Bf6 8. Qc1',
        'Nc6 9. d3 Bxb2 10. Qxb2 Qf6 11. Qxf6 Nxf6 12. Nc3 d6 13. Rab1 Bd7 14. Rfc1 a6',
        '15. b4 h6 16. d4 Rae8 17. e3 Nd8 18. a4 g5 19. a5 f4 20. exf4 gxf4 21. b5 fxg3',
        '22. hxg3 Ng4 23. Rb2 Kg7 24. Ne4 Nf7 25. Nh2 Nxh2 26. Kxh2 Rb8 27. Kg1 Rfc8 28.',
        'Rcb1 axb5 29. cxb5 Ra8 30. Ra2 Ra7 31. a6 Rca8 32. Nc3 d5 33. Nxd5 exd5 34.',
        'Bxd5 Rd8 35. axb7 Rxa2 36. Bxa2 Nd6 37. b6 c6 1/2-1/2',
        '',
        ))

    print datetime.datetime.now().isoformat()
    pgn = PGNReader()
    #source = open('/usr/home/roger/games_in_pgn/pgn/Crafty06.pgn', 'rbU')
    source = cStringIO.StringIO(pgndata)
    gamecount = 0
    movecount = 0
    #positioncount = 0
    #positionlength = 0
    try:
        for d in pgn.get_games(source):
            pgn.process_game()
            gamecount += 1
            movecount += len(pgn.tokens)
            #positioncount += len(pgn.positions)
            #positionlength += sum([len(p) for p in pgn.positions])
    except:
        print pgn._token_groups
        print
        print pgn.tokens
        print
        print pgn.piece_locations
        print
        print pgn.occupied_square_pieces
        print
        print pgn.side_to_move
        raise
    source.close()
    print datetime.datetime.now().isoformat()
    print gamecount, movecount#, positioncount, positionlength / positioncount
    print pgn._tags_valid, pgn.is_tag_roster_valid()
    