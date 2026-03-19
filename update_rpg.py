def main():
    try:
        with open('c:/My_portfolio/index.html', 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Read error: {e}")
        return

    old_css = """        /* Profile card */
        .prof-card {
            position: relative;
            width: 100%;
            max-width: 380px;
            justify-self: center;
            border-radius: 14px;
            overflow: hidden;
            transition: .5s
        }

        .prof-card::before {
            content: '';
            position: absolute;
            inset: -2px;
            z-index: -1;
            border-radius: 16px;
            background: conic-gradient(from 0deg, var(--violet), var(--neon-blue), var(--gold), var(--violet));
            animation: rotBorder 4s linear infinite;
            opacity: .5;
            transition: opacity .5s
        }

        .prof-card:hover::before {
            opacity: 1
        }

        @keyframes rotBorder {
            to {
                transform: rotate(360deg)
            }
        }

        .prof-inner {
            background: #0c0c1d;
            border-radius: 14px;
            padding: 8px;
            position: relative
        }

        .prof-img {
            width: 100%;
            height: 440px;
            object-fit: cover;
            border-radius: 10px;
            filter: saturate(.85) contrast(1.1);
            transition: filter .5s
        }

        .prof-card:hover .prof-img {
            filter: saturate(1.1) contrast(1.15)
        }

        .badge {
            position: absolute;
            bottom: 18px;
            left: 18px;
            background: rgba(2, 4, 10, .8);
            backdrop-filter: blur(10px);
            padding: 10px 18px;
            border-radius: 6px;
            font-family: var(--font-ui);
            font-weight: 700;
            font-size: .65rem;
            letter-spacing: 2px;
            border: 1px solid rgba(255, 255, 255, .08);
            color: var(--neon-blue);
            animation: badgePulse 2s ease-in-out infinite
        }

        @keyframes badgePulse {

            0%,
            100% {
                box-shadow: 0 0 10px rgba(0, 242, 255, .2)
            }

            50% {
                box-shadow: 0 0 25px rgba(0, 242, 255, .5)
            }
        }"""
    
    new_css = """        /* Profile RPG Card */
        .prof-card {
            position: relative;
            width: 100%;
            max-width: 380px;
            justify-self: center;
            border-radius: 14px;
            overflow: hidden;
            transition: .5s;
        }

        .prof-card::before {
            content: '';
            position: absolute;
            inset: -2px;
            z-index: -1;
            border-radius: 16px;
            background: conic-gradient(from 0deg, var(--violet), var(--neon-blue), var(--gold), var(--violet));
            animation: rotBorder 4s linear infinite;
            opacity: .5;
            transition: opacity .5s;
        }

        .prof-card:hover::before {
            opacity: 1;
        }

        @keyframes rotBorder {
            to { transform: rotate(360deg); }
        }

        .prof-inner {
            background: #0c0c1d;
            border-radius: 14px;
            padding: 8px;
            position: relative;
        }

        .prof-img-wrapper {
            position: relative;
            overflow: hidden;
            border-radius: 10px 10px 0 0;
            margin: -8px -8px 0 -8px;
            background: #000;
        }

        .prof-img {
            width: 100%;
            height: 320px;
            object-fit: cover;
            object-position: top;
            filter: saturate(0.85) contrast(1.1);
            transition: filter .5s, transform .8s cubic-bezier(0.16, 1, 0.3, 1);
        }

        .prof-card:hover .prof-img {
            transform: scale(1.08);
            filter: saturate(1.1) contrast(1.15);
        }

        .prof-overlay {
            position: absolute;
            inset: 0;
            background: linear-gradient(to top, #0c0c1d 0%, transparent 50%);
            pointer-events: none;
        }

        .ui-corner {
            position: absolute;
            width: 20px;
            height: 20px;
            border: 2px solid var(--neon-blue);
            z-index: 2;
            pointer-events: none;
            transition: .4s;
        }
        .ui-corner.top-left { top: 10px; left: 10px; border-right: none; border-bottom: none; }
        .ui-corner.top-right { top: 10px; right: 10px; border-left: none; border-bottom: none; }
        .ui-corner.bot-left { bottom: 10px; left: 10px; border-right: none; border-top: none; }
        .ui-corner.bot-right { bottom: 10px; right: 10px; border-left: none; border-top: none; }

        .prof-card:hover .ui-corner {
            width: 30px;
            height: 30px;
            border-color: var(--gold);
        }

        .prof-details {
            padding: 25px 15px 10px;
            text-align: center;
            position: relative;
            z-index: 3;
            margin-top: -30px;
        }

        .char-name {
            font-family: var(--font-ui);
            font-size: 1.4rem;
            color: #fff;
            letter-spacing: 3px;
            margin-bottom: 2px;
            text-shadow: 0 0 10px rgba(0,242,255,0.5);
            text-transform: uppercase;
        }

        .char-class {
            font-family: var(--font-ui);
            font-size: 0.65rem;
            color: var(--gold);
            letter-spacing: 4px;
            margin-bottom: 22px;
            text-transform: uppercase;
        }

        .char-stats {
            margin-bottom: 20px;
            text-align: left;
            padding: 0 5px;
        }

        .stat-row {
            margin-bottom: 12px;
        }

        .stat-row span {
            font-family: var(--font-ui);
            font-size: 0.6rem;
            color: rgba(255,255,255,0.6);
            letter-spacing: 2px;
            display: block;
            margin-bottom: 6px;
        }

        .stat-bar {
            width: 100%;
            height: 6px;
            background: rgba(255,255,255,0.05);
            border-radius: 3px;
            overflow: hidden;
            box-shadow: inset 0 0 5px rgba(0,0,0,0.5);
            position: relative;
        }

        .stat-fill {
            height: 100%;
            border-radius: 3px;
            box-shadow: 0 0 10px currentColor;
            position: relative;
        }
        
        .stat-fill::after {
            content: '';
            position: absolute;
            top: 0; right: 0; bottom: 0; left: 0;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.8), transparent);
            background-size: 200% 100%;
            animation: shimmer 2s linear infinite;
        }

        .prof-inner .badge {
            display: block;
            width: 100%;
            box-sizing: border-box;
            background: rgba(2, 4, 10, .8);
            backdrop-filter: blur(10px);
            padding: 12px 18px;
            border-radius: 6px;
            font-family: var(--font-ui);
            font-weight: 700;
            font-size: .75rem;
            letter-spacing: 3px;
            border: 1px solid rgba(0, 242, 255, .3);
            color: var(--neon-blue);
            animation: badgePulse 2s ease-in-out infinite;
            text-transform: uppercase;
        }

        @keyframes badgePulse {
            0%, 100% { box-shadow: 0 0 10px rgba(0, 242, 255, .2), inset 0 0 10px rgba(0, 242, 255, .05); }
            50% { box-shadow: 0 0 25px rgba(0, 242, 255, .5), inset 0 0 20px rgba(0, 242, 255, .1); }
        }"""

    old_html = """                <div class="prof-card">
                    <div class="prof-inner">
                        <img src="assets/projects/me.jpeg" alt="Profile" class="prof-img">
                        <div class="badge">STATUS: FRESHER</div>
                    </div>
                </div>"""

    new_html = """                <div class="prof-card" id="rpgCard">
                    <div class="prof-inner">
                        <div class="prof-img-wrapper">
                            <img src="assets/projects/me.jpeg" alt="Player Character" class="prof-img">
                            <div class="prof-overlay"></div>
                            <div class="ui-corner top-left"></div>
                            <div class="ui-corner top-right"></div>
                            <div class="ui-corner bot-left"></div>
                            <div class="ui-corner bot-right"></div>
                        </div>

                        <div class="prof-details">
                            <h3 class="char-name">PRATHEEN</h3>
                            <p class="char-class">LVL 1 • GAME DEVELOPER</p>
                            
                            <div class="char-stats">
                                <div class="stat-row">
                                    <span>CREATIVITY [INT]</span>
                                    <div class="stat-bar"><div class="stat-fill" style="width: 85%; background: var(--violet); color: var(--violet);"></div></div>
                                </div>
                                <div class="stat-row">
                                    <span>LOGIC [WIS]</span>
                                    <div class="stat-bar"><div class="stat-fill" style="width: 90%; background: var(--neon-blue); color: var(--neon-blue);"></div></div>
                                </div>
                                <div class="stat-row">
                                    <span>PASSION [STM]</span>
                                    <div class="stat-bar"><div class="stat-fill" style="width: 95%; background: var(--gold); color: var(--gold);"></div></div>
                                </div>
                            </div>
                            
                            <div class="badge">STATUS: FRESHER</div>
                        </div>
                    </div>
                </div>"""

    if old_css in content:
        content = content.replace(old_css, new_css)
        print("CSS replaced!")
    else:
        print("CSS not found!")

    if old_html in content:
        content = content.replace(old_html, new_html)
        print("HTML replaced!")
    else:
        print("HTML not found!")

    try:
        with open('c:/My_portfolio/index.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("Success")
    except Exception as e:
        print(f"Write error: {e}")

if __name__ == '__main__':
    main()
