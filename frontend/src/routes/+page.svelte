<script>
    import hc from "$lib/assets/hc.svg"

    let dmtxt = $state("dark mode")

    function darkmode() {
      const root = document.documentElement;
      const currentTheme = root.getAttribute('data-theme');
      const nextTheme = currentTheme === 'dark' ? 'light' : 'dark';

      dmtxt = currentTheme + " mode"
      root.setAttribute('data-theme', nextTheme);
    };
</script>

<div class="page">
    <div class="header">
        <div class="header-item left">
            <div class="hc">
                <img class="hc-logo" src="{hc}" width="var(--size-header);" alt="Hack Club">
                <span class="hc-text">Hack Club</span>
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
</div>
<button class="darkmode" onclick={darkmode}>{dmtxt}</button>

<style>
    .page {
        max-width: 800px;
        width: 100%;
        min-height: 110vh;
        background-color: var(--fg);
        justify-self: center;

        padding: 0px;

        transform: translateY(30vh);
        opacity: 0.5;
        animation: slideInTop 0.6s ease-out both;

        border: 2px var(--dim) outset;
    }

    .darkmode {
        position: absolute;
        top: 10px;
        left: 10px;
        background-color: var(--dim);
        border-color: var(--pm);
        color: var(--ac);
        font-weight: bold;
        font-family: monospace;
    }

    .header {
        display: flex;
        justify-content: space-between;
        font-size: var(--font-header);
        font-weight: 500;

        padding: 4px 8px;
    }

    .callout {
        display: flex;
        background-color: var(--dimmer);
        color: var(--pm);
        font-family: monospace;
        font-weight: 800;
        font-size: 0.5rem;
        line-height: 1em;
        white-space: pre;
        justify-content: center;

        border-top: var(--ac);
        border-bottom: var(--ac);
        border-left: transparent;
        border-right: transparent;
        border-width: 4px;
        border-style: inset;
        padding: 8px 0px;
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
        gap: 8px;
    }

    .hc-logo { height: var(--font-header); }
    .hc-text { color: var(--hc); text-decoration: underline; }

    @keyframes slideInTop {
        from {
            transform: translateY(30vh);
            opacity: 0.5;
        }
        to {
            transform: translateY(0px);
            opacity: 1;
        }
    }

</style>
