<script>
    import hc from "$lib/assets/hc.svg"
    import PrizeTable from "$lib/PrizeTable.svelte";
    import Questions from "$lib/Questions.svelte";

    /* let dmtxt = $state("dark mode")
    function darkmode() {
      const root = document.documentElement;
      const currentTheme = root.getAttribute('data-theme');
      const nextTheme = currentTheme === 'dark' ? 'light' : 'dark';
      dmtxt = currentTheme + " mode"
      root.setAttribute('data-theme', nextTheme);
    }; */
</script>

<div class="page">
    <div class="header">
        <div class="header-item left">
            <div class="hc">
                <img class="hc-logo" src="{hc}" width="var(--font-header);" alt="Hack Club">
                <span class="hc-text"><a href="https://hack.club">Hack Club</a></span>
            </div>
            <span>Request for Comments: 727</span>
            <span>Category: YSWS</span>
        </div>
        <div class="header-item right">
            <span>Dawn, A</span>
            <span>Jolly, W</span>
            <span>July XX, 2026</span>
        </div>
    </div>
    <div class="callout">
        <div class="callout-at">
                     &nbsp;
               .-++##############+-.
           .-+#######################+-.
        .-+#####+.-#############+.-+####+-
       -+###+ +#####################+.-###+-
     .-##+--+####+-.           .-+####+.-+##-.
    .+##-.+##+-.                   .-+##-.-##+.
   .+#+.-##+-      .-+#####+-..--++-. -##+..+#+.
  .+#-..##-.    .-##################+  .+#+..+#-.
  -#+..+#-     -####-.-+##+.-+#+---##   .-#+ .##-
 .##. -#+.   .-##+.-##########-..  ##    .##- -#+
 -#+ .##.    -##-.+##+-....-+##-.  ##     -#- .##.
 +#- .#+    .##- +#+.        .##.  ##     .#+  ##.
 ##. -#-    -#+ .##.          -#-  ##     .#+  +#.
.##. +#-    -#- -#-           .#+  ##     .#+  ##.
.##. -#-    -#- -#+           -#+  ##     .#+ .##.
 ##. -#+    -#+ .##.          +#-  ##     -#+ .#+
 +#- .#+    .+#- +#+.        -##.  ##    .+#- -#-
 -#+..+#-    -##..+##+-. ..-+##-.  +#-  .+#+..##.
 .+#. -#+.   .-##-.+#########+.+-. -######+.-##-.
  -#+..+#+.   .-###+.-+###+.-#####+-.+###-.+##-.
  .+#+..+#+.    .+############---############-.
   .+#+..+##+.    .-+######+-.   .-+######+-.
    .+##- -###+-.
     .-###- -######+--..     ..--+###-.
       -+###+-.+######################-
         .+######+-.-+########+-..-###-
            .+#######################+-
                .--+############++-.
                        &nbsp;
        </div>
        <div class="callout-name"></div>
    </div>
    <div class="body">
        <h1>0. Abstract</h1>
        <h2>You Ship:</h2>
        <p>A project that uses or implements a protocol without a library.</p>
        <h2>We Ship:</h2>
        <p>Free prizes (!!!) related to your project!</p>
    </div>
    <div class="callout">
        sign up
    </div>
    <div class="body">
        <hr>
        <h1>1. You Ship</h1>
        <p>
            Find a project idea that moves information between two pieces of tech.
            Then, instead of relying on a library, learn how a protocol works and
            implement it yourself!
        </p>
        <p>
            Some examples of common protocols and things you might make with them:
        </p>
        <PrizeTable/>
        <p>
            Track the time you spent building with
            <a href="https://hackatime.hackclub.com" target="_blank">Hackatime</a>
            and use version control (like GitHub) to track your progress over time.
        </p>
        <hr>
        <h1>2. We Ship</h1>
        <p>
            Write a README for people to see, package your project, submit it here,
            and share it with the world! Then, spend the time you've logged on your
            pick of prizes from the shop, and we'll send them to you for free:
        </p>
    </div>
    <div class="callout">
        <div class="track">
            <div class="prize">
                <div class="prize-art">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;########
       ##------##
 #######-.##+-.-#######
###---##-.####.-##---###
#++#+--##+----+##--+#++#
#+--+#+-+######+-+#+--+#
#+----+#+------+#+----+#
#+---+####+--+####+---+#
#+-+##+--++##++--+##+-+#
####+--------------+####
########################
                </div>
                <div class="prize-name">
                    1yr Purelymail
                </div>
            </div>
            <div class="prize">
                meow
            </div>
        </div>
    </div>
    <div class="body">
        <hr style="margin-top: var(--pad-s);">
        <h1>3. Questions</h1>
        <Questions/>
        <p><em>
            More questions? Ask in
            <a href="https://hackclub.enterprise.slack.com/archives/C0BGPHJV9P1" target="_blank">#at-ysws</a>
            or email @
            <a href="mailto:beans@beans.beans">ADD@EMAIL.HERE</a>
        </em></p>
        <hr>
        <h1>4. Sign Up</h1>
        <p>Sound interesting? Sign in with Hack Club and you'll get an email when we're ready for you to start building.</p>
    </div>
    <div class="callout">
        sign up
    </div>
    made with love etc
</div>

<style>
    .page {
        display: flex;
        flex-direction: column;
        gap: var(--gap-s);
        max-width: 75rem;
        width: 100%;
        background-color: rgb(from var(--bg) r g b / 50%);
        backdrop-filter: blur(10px);
        margin-inline: auto;

        padding: var(--pad-v) 0px;

        opacity: 0.2;
        animation: slideInTop 0.6s ease-out both;

        border: var(--border-sm) var(--bg) inset;
    }

    .header {
        display: flex;
        justify-content: space-between;
        font-size: var(--font-header);
        font-weight: 500;

        padding: 0px var(--pad-h);
    }

    .header-item {
        display: flex;
        flex-direction: column;
    }

    .left { text-align: left; }
    .right { text-align: right; }

    .hc {
        display: flex;
        flex-direction: row;
        align-items: center;
        gap: var(--gap-s);
    }

    .hc-logo { height: var(--font-header); }
    .hc-text { color: var(--hc); text-decoration: underline; }

    .callout {
        display: flex;
        flex-direction: column;
        align-items: center;
        background-color: rgb(from var(--dimmer) r g b / 50%);
        color: var(--pm);
        font-family: monospace;
        font-weight: 800;
        letter-spacing: 0.04rem;
        font-size: var(--font-ascii);
        line-height: 1em;
        white-space: pre;
        justify-content: center;
        user-select: none;

        border-block: var(--border-lg) outset var(--ac);
        border-inline-color: transparent;
        padding: var(--pad-v) 0px;
        margin-bottom: var(--gap-s);
    }

    .callout-name {
        font-weight: bold;
        letter-spacing: 0rem;
        line-height: 1em;
        text-align: center;
    }

    .body {
        padding: 0px var(--pad-h);
        line-height: 1.2;
    }

    .track {
        display: flex;
        flex-direction: row;
        gap: var(--gap-s)
    }

    .prize {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: space-between;
        border: var(--border-sm) solid var(--dim);
        border-radius: 1rem;
        gap: var(--gap-s);
        padding: var(--pad-s);
        min-width: 6rem;
    }

    .prize-art {
        font-family: monospace;
        font-weight: 800;
        letter-spacing: 0.04rem;
        font-size: var(--font-ascii);
        line-height: 1em;
        white-space: pre;
    }

    .prize-name {
        font-size: 1rem;
        font-weight: 400;
        user-select: text;
    }

    .list {
        display: flex;
        align-items: center;
        font-size: var(--font-header);
        gap: var(--gap-s);
        line-height: 1.25;
        margin: --pad-s 0px;
    }

    @keyframes slideInTop {
        from {
            opacity: 0.2;
        }
        to {
            opacity: 1;
        }
    }

    @media (width < 800px) {
        :root {
            margin: 1rem;
        }
    }
    @media (width < 500px) {
        :root {
            margin: 0.2rem;
        }
    }
</style>
