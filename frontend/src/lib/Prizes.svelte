<script>
  import { onMount } from "svelte";
  import wsl from '$lib/assets/ws.json';

  let ws = [...wsl];
  for (let i = ws.length - 1; i > 0; i--) {
  	const j = Math.floor(Math.random() * (i + 1));
  	[ws[i], ws[j]] = [ws[j], ws[i]];
  }

  let wss = ws
</script>

<div class="carousel">
    <div class="track">
        {#await wss}
            <div>loading...</div>
        {:then}
            {#each wss as prize}
                <div class="prize">
                    <div class="prize-art">
                        {#each prize.art as art_ln}
{art_ln}<br>
                        {/each}
                    </div>
                    <div class="prize-name">
                        {prize.name}
                    </div>
                </div>
            {/each}

            <!-- again bcz css is css -->
            {#each wss as prize}
                <div class="prize">
                    <div class="prize-art">
                        {#each prize.art as art_ln}
{art_ln}<br>
                        {/each}
                    </div>
                    <div class="prize-name">
                        {prize.name}
                    </div>
                </div>
            {/each}
        {/await}
    </div>
</div>

<style>
    .carousel {
        width: 100%;
        overflow: hidden;
        position: relative;
        margin: 0 auto;
    }

    .track {
        display: flex;
        flex-direction: row;
        gap: var(--gap-s);
        padding: var(--pad-s) 0px;

        width: max-content;
        animation: scroll 25s linear infinite;
    }

    .track::-webkit-scrollbar {
      display: none;
    }

    .track:hover,
    .track:active {
      animation-play-state: paused;
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
        flex-shrink: 0;
    }

    .prize-art {
        font-family: monospace;
        font-weight: 800;
        letter-spacing: 0.04rem;
        font-size: var(--font-ascii);
        line-height: 1em;
        white-space: pre;
        margin: 0px;
        padding: 0px;
    }

    .prize-name {
        font-size: 1rem;
        font-weight: 400;
        user-select: text;
    }

    @keyframes scroll {
      0% {
        transform: translateX(0);
      }
      100% {
        transform: translateX(calc(-50% - 8px));
      }
    }
</style>
