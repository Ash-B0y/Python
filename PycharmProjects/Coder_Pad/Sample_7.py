from difflib import SequenceMatcher
import re
Movie_one = ''
Movie_two = ''
Movie_list = ['1408 (2007)', '1408 ', '21 & Over (2013)', '47.Ronin.2013.720p.BluRay.x264.YIFY.mp4', '50 First Dates (2004) [Eng] [DVDrip].avi', '500.Days.Of.Summer.BDRip.XviD-ARiGOLD', '9C Oslo (2016).mkv', 'A Beautiful Mind (2001)', 'A Man Apart.mp4', 'A MOMENT TO REMEMBER(2004)DVDRIP.XVID-PJRV AND PRG RELEASE', 'A Walk Among the Tombstones (2014) [1080p]', 'Abraham Lincoln Vampire Hunter 2012 BRRip 720p x264 [English.Hindi.Tamil.Telugu.Audio]-ViZNU[P2PDL]', 'Ace Ventura_ Pet Detective (1994) [1080p]', 'American Pie series', 'Anna (2013)', 'Anna Karenina (2012)', 'Another Me', 'ARGO DVDRIP EDAW2013', 'As Good As it Gets', 'As Good As IT Gets(Xvid)(Darkside_RG).avi', 'August Rush', 'Bad News Bears 2005 DvDRip XviD AC3[ 2Ch 6Ch ] ESubsM777 M2Tv', 'Battleship (2012) [1080p]', 'Baywatch (2017).mkv', 'Before I Go to Sleep (2014)', 'Before Sunrise', 'Better Life', 'Big.Miracle.2012.DVDRip.XviD-SCREAM', 'Bighero', 'Blood Diamond (2006) [1080p]', 'Boyhood (2014)', 'Brick Mansions (2014)', 'Bridge Of Spies (2015) [YTS.AG]', 'Brothers (2009)', 'Captain America The Winter Soldier (2014)', 'Chappie (2015)', "Charlie's Angel's Series", 'Chinese Zodiac (2012)  WEBRiP XViD - RiSES', 'Cliffhanger.1993.720p.Bluray.x264.YIFY.mp4', 'Cloverfield[2008]DvDrip.AC3[Eng]-aXXo', 'coming to america.avi', 'Crank           [1-2]', 'crazy stupid love 2011', 'DC collection', 'deadpool', 'December Boys[2007]DvDrip[Eng]-FXG', 'Deja.Vu[2006]DvDrip[Eng]-aXXo', 'Departures.[Okuribito].2008.BluRay.480p.H264', 'Despicable Me 3 (2017) [1080p] [YTS.AG]', 'Django Unchained', 'Dolphin Tale', 'Donnie Darko DIRECTORS CUT (2001)', 'Dont.Breathe.2016.720p.BluRay.H264.AAC-RARBG', 'Eddie.the.Eagle.2016.720p.BRRip.x264.AAC-ETRG', 'Edge of Tomorrow (2014) [1080p]', 'Elysium (2013)', 'End of Watch', 'Enders game', 'Enemy 2013 (1080p Bluray x265 HEVC 10bit AAC 5.1 Tigole)', 'Enemy At The Gates (2001) [1080p]', 'Eternal Sunshine of the Spotless Mind', 'euro trip', 'Ex Machina (2015)', 'Exodus.Gods.and.Kings.2014.720p.BluRay.x264.YIFY.mp4', 'Exorcism of Emily Rose [Unrated] [2005].mp4', 'fast n furious', 'FEARLESS', 'fifty_shades_of_grey_2015_uncut_hc_hdrip_800mb_mkvcage', 'Fighter', 'Final Girl (2015)', 'fired up', 'Flipped (2010) 720p BrRip x264 - YIFY', 'Focus.2015.HC.HDRip.XviD.AC3-EVO.avi', 'Forrest Gump. XviD.avi', 'Fury (2014)', 'G.I.Joe Retaliation [2013]-Extended ActionCut-720p-BRrip-x264-StyLishSaLH (StyLish Release)', 'get away', 'Godfather Trilogy', 'Good Luck Chuck [2007]', 'Green.Room.2015.720p.BRRip.x264.AAC-ETRG', "Gulliver's Travels[2010]", "He's Just Not That Into You[2009]DvDrip[Eng]-FXG", 'Her (2013)', 'Hitman.Agent.47.2015.720p.BRRip.x264.AAC-ETRG', 'Honeymoon (2014)', 'Horrible Bosses (2011)', 'Hostage (2005)', 'Hostel [1-2-3]', 'Hotel Rwanda (2004) DVDrip. Xvid', 'Housebound (2014)', 'How.To.Be.Single.2016.720p.BluRay.x264-[YTS.AG].mp4', 'HULK ~ (BLURAY SERIES)', 'I am Number Four', 'I,Frankenstein', 'If I Stay', 'if only', 'Inside out', 'Insomnia (2002)', 'Into the Storm (2014) [1080p]', 'Into the Woods (2014)', 'Invictus[2009]DvDrip[Eng]-FXG', 'IP Man', 'It Follows (2014)', 'Jack Reacher (2012)', 'Jack Reacher Never Go Back (2016) [YTS.AG]', 'Jack Ryan Shadow Recruit (2014)', 'jOBS (2013)', 'Karate Kid', 'Kick-Ass 2 2013 R6 720p WEBRip x264 AAC-JYK.mkv', 'Kill Bill Series', 'Kingsman.The.Secret.Service.2014.HC.HDRip.900MB.MkvCage.mkv', 'Kung Fu Panda Series', 'Le concert (2009)', 'Legend.of.the.Fist.The.Return.of.Chen.Zhen.2010.DvDRip.XviD.Feel-Free', 'Life of Pi (2012) [1080p]', 'Life.Is.Beautiful.-.La.Vita.è.Bella.-.1997.Eng.544.24fps.705kbps.V5.WunSeeDee', 'Lights Out 2016 1080p BRRip x264', 'Limitless (2011) 1080p', 'Lockout (2012)', 'lord of the rings', "Madagascar 3 Europe's Most Wanted ~ 2012 ~ DVD-Rip ~ X264 ~ Multi Audio ~ 700MB ~ Uyirvani.com.mkv", 'Man.on.a.Ledge.2012.720p.BluRay.x264.YIFY.mp4', 'Million.Dollar.Baby[2004]DvDrip[Eng]-TB.avi', 'Mud [2012].mkv', 'Neighbors.2014.720p.BluRay.x264.YIFY.mp4', 'Now.You.See.Me.2.2016.720p.BRRip.x264.AAC-ETRG.mp4', 'Pacific.Rim.2013.720p.BluRay.x264.YIFY.mp4', 'Phone.Booth.2002.720p.BluRay.DTS.x264-XSHD.mkv', 'Pompeii (2014)', 'predator', 'Predestination', 'Premium Rush (2012)', 'Prisoners (2013)', 'Proof (2005)', 'PS.I.Love.You.[2007.Eng].DVDrip.DivX-LTT', 'Pubic Enemies (2009)', 'Pulp Fiction (1994)', 'Rec.2007.READNFO.DVDRiP.XViD-iKA.[Hardcoded.English.Subtitles]', 'Red 2 (2013)', 'Reddick', 'Reservoir Dogs (1992)', 'Resident evil', 'Ring', 'Road to Paloma (2014)', 'Roadside.Romeo.2008.DVDRip.XviD', 'Saving Private Ryan', 'Schindlers.List.1993.INTERNAL.DVDRip.XviD-PARTiCLE', 'Season of the Witch (2011) DVDRip XviD-MAXSPEED www.torentz.3xforum.ro.avi', 'Sex Tape (2014)', 'Shallows.mkv', 'Sherlock series', 'shooter', 'Silent.Hill[2006]DvDrip[Eng]-aXXo', 'Sin City EXTENDED and UNRATED (2005)', 'Skiptrace.2016.HDRip.AC3.2.0.x264-BDP', 'Sleepless in Seattle (1993) [ENG] [DVDrip]', 'Snitch.2013.720p.BluRay.x264.YIFY.mp4', 'Southpaw.2015.720p.BRRip.x264.AAC-ETRG', 'Spotlight (2015) [YTS.AG]', 'Steve.Jobs.2015.BRRip.XviD.AC3-RARBG', 'Suicide.Squad.2016.720p.HC.HDRip.2CH.x265.HEVC.mkv', 'TARZAN ~ (HD)', 'The Aviator (2004) [1080p]', 'The Awakening', 'The Babadook (2014) [1080p]', 'The Boss Baby (2017) [1080p] [YTS.AG]', 'the bourne series', 'The Butterfly Effect (2004) BluRay 720p 800MB Ganool', 'The Cabin in the Woods (2011)', 'The Colony 2015', 'The Curious Case Of Benjamin Button', 'the dark shadows', 'The Darkest Hours[2011]BRRip XviD-ETRG', 'The Descent', 'The Double', 'The Dreamers', 'The DUFF 2015 English Movies 720p BluRay x264 AAC with Sample ~ ☻rDX☻ - Copy', 'The Dyatlov Pass Incident (2013)', 'The Gambler (2014)', 'The Giver (2014)', 'The Good, the Bad and the Ugly-Extended [1966]-720p-BRrip-x264-StyLishSaLH', 'The Grand Budapest Hotel (2014)', 'The Great Gatsby', 'The Hangover I, II, III', 'The hateful 8', 'The Hobbit The Desolation of Smaug (2013)', 'The Hurt Locker (2009) DVDR DivXNL-Team', 'The Imitation Game 2014 DVDScr x264 AC3-JYK', 'The Judge (2014)', 'The Kingdom[2007]DvDrip[Eng]-FXG', 'The Martian (2015) [YTS.AG]', 'The Maze Runner Series', 'The Mechanic 2011', 'The Peanuts', 'The Shawshank Redemption (1994)', 'The Sixth Sense', 'The Smurfs 2', 'The Terminal', 'The Theory of Everything (2014) [1080p]', 'The Three Musketeers.avi', 'The Visit', 'The.Big.Short.2015.DVDScr.XVID.AC3.HQ.Hive-CM8', 'The.Bridge.on.the.River.Kwai[1957].Dvdrip.Xvid.AC3[5.1]-RoCK', 'The.Bucket.List[2007]DvDrip-aXXo', 'The.Descendants.2011.DVDSCR.XviD-GooN', 'The.Fountain[2006]DvDrip[Eng]-aXXo', 'The.Good.Lie.2014.720p.BluRay.x264.YIFY.mp4', 'The.Happening[2008]DvDrip-aXXo', 'The.Last.Song.2010.DVDRip.XviD-ZMG', 'The.Man.Who.Knew.Infinity.2015.720p.BluRay.HEVC.x265.mkv', 'The.Number.23[2007][Unrated.Edition][DvDrip[Eng]-aXXo.avi', 'The.Perfect.Game.2009.DVDRip.XviD.AC3-ARROW [www.extratorrent.com]', 'The.Silence.Of.The.Lambs.1991.720p.BluRay.X264.YIFY.mp4', 'Think Like A Man', 'This.Is.Where.I.Leave.You.2014.720p.BluRay.x264.YIFY.mp4', 'Thor.The.Dark.World.2013.720p.WEB-DL.H264-WEBiOS [PublicHD]', 'Titanic.1997.nHD.720p.x264.NhaNc3.mkv', 'Transcendence (2014)', 'Transformers 3 Dark of the Moon 2011.SWESUB.TS XViD', 'Transporter series', 'Triangle - Mystery Thriller 2009 Eng Subs 720p [H264-mp4]', 'twilight', 'unbreakable', 'Underworld', 'Up In The Air (2009)', 'Up Pixar [2009] dvd rip nlx', 'Van Helsing', 'Vertical Limit', 'V_for_Vendetta_(2006)_[1080p]', 'We.Bought.A.Zoo [2011]', "Winter's Tale (2014)", 'YOU DONT MESS WITH ZOHAN ~ (BLURAY)', 'Zero Dark Thirty [2012]-720p-BRrip-x264-StyLishSaLH (StyLish Release)', 'Zodiac (2007)', 'Zootopia.2016.720p.HDRiP.MP3.650MB.mkv']
Movie_extensions = ['.avi', '.mp4', '.mkv', '.flv', '.mov']
Movie_release_formats = ['CAM-Rip','CAM','TS','HDTS','TELESYNC','PDVD','PreDVDRip','WP','WORKPRINT','TC','HDTC','TELECINE','PPV','PPVRip','SCR','SCREENER','DVDSCR','DVDSCREENER','BDSCR','DDC','R5','R5.LINE','R5.AC3.5.1.HQ','DVDRip','DVDMux','DVDR','DVD-Full','Full-Rip','ISO rip','lossless rip','untouched rip','DVD-5','DVD-9','DSR','DSRip','SATRip','DTHRip','DVBRip','HDTV','PDTV','DTVRip','TVRip','HDTVRip','WEBDL','WEB DL','WEB-DL','HDRip','WEB-DLRip','WEBRip(P2P)','WEB Rip(P2P)','WEB-Rip(P2P)','WEB(Scene)','HC','HD-Rip','Blu-Ray','BluRay','BLURAY','BDRip','BRip','BRRip','BDMV','BDR','BD25','BD50','BD5','BD9','WEB-Cap','WEBCAP','WEB Cap']
Similar_Movies = {}
Movie_list.sort()
for i in range(0, len(Movie_list)):
    Movie_1 = []
    if '(' in Movie_list[i]:
        Movie_one = Movie_list[i][0: Movie_list[i].index('(')]
    elif '[' in Movie_list[i]:
            Movie_one = Movie_list[i][0: Movie_list[i].index('[')]
    elif '.' in Movie_list[i]:
        Movie_1 = re.findall(r'[1-2][0-9][0-9][0-9]', Movie_list[i])
        if not Movie_1:
            res = [x for x in Movie_extensions if re.search(x, Movie_list[i])]
            if res:
                Movie_one = Movie_list[i][0:Movie_list[i].find(res[0])]
            else:
                res = [x for x in Movie_release_formats if re.search(x, Movie_list[i])]
                Movie_one = Movie_list[i][0:Movie_list[i].find(res[0])]

        else:
            Movie_one = Movie_list[i][0:Movie_list[i].index(Movie_1[0][0])]

    for j in range(i+1, len(Movie_list)):
        print(Movie_list[j])
        Movie_2 = []
        if '(' in Movie_list[j]:
            Movie_two = Movie_list[j][0: Movie_list[j].index('(')]
        elif '[' in Movie_list[j]:
            Movie_two = Movie_list[j][0: Movie_list[j].index('[')]
        elif '.' in Movie_list[i]:
            Movie_1 = re.findall(r'[1-2][0-9][0-9][0-9]', Movie_list[i])
            if not Movie_1:
                res = [x for x in Movie_extensions if re.search(x, Movie_list[i])]
                if res:
                    Movie_one = Movie_list[i][0:Movie_list[i].find(res[0])]
                else:
                    res = [x for x in Movie_release_formats if re.search(x, Movie_list[i])]
                    Movie_one = Movie_list[i][0:Movie_list[i].find(res[0])]

            else:
                Movie_one = Movie_list[i][0:Movie_list[i].index(Movie_1[0][0])]


        print(str(Movie_two))
        if SequenceMatcher(a=str(Movie_one), b=str(Movie_two)).ratio() > 0.6:

            if Movie_list[i] not in Similar_Movies.keys():
                Similar_Movies.setdefault(Movie_list[i], []).append(Movie_list[j])
                #del Movie_list[j]
            else:
                Similar_Movies[Movie_list[i]].append(Movie_list[j])
                #del Movie_list[j]

    #del Movie_list[i]
print(Similar_Movies)
