<script>
  import { onMount } from "svelte";
  import ys from '$lib/assets/ys.json';

  /*onMount(async () => {
    try {
      const res =  await fetch("/ys.json");
      ys = await res.json()
    } catch (error) {
      console.error("Failed to load YS items:", error)
    }
  })
 */
</script>

<div class="tiles">
    {#await ys}
        <div>loading...</div>
    {:then}
        {#each ys as tile}
            <div class="tile">
                <span class="tile-head">{tile.name}</span>
                <div class="tile-body">
                    <div class="tile-part">
                        <div class="tile-l"> YS </div>
                        <div class="tile-r">
                            {#each tile.ys as example}
                                <span class="item"><at>@</at> {example} </span>
                            {/each}
                        </div>
                    </div>
                    <div class="tile-part">
                        <div class="tile-l tlb"> WS </div>
                        <div class="tile-r">
                            {#each tile.ws as prize}
                                <span class="item"><at>@</at> {prize} </span>
                            {/each}
                        </div>
                    </div>
                </div>
            </div>
        {/each}
    {/await}
</div>

<style>
    .tiles {
        display: flex;
        flex-wrap: wrap;
        width: 100%;
        gap: var(--gap-l);
        margin-top: var(--pad-v);
    }

    .tile {
        display: flex;
        flex-grow: 1;
        white-space: nowrap;
        flex-direction: column;
        border: var(--border-sm) solid var(--ac);
        border-radius: 1rem;
    }

    .tile-body {
        font-size: var(--font-body);
        display: flex;
        flex-direction: column;
        flex-grow: 1;
    }

    .tile-part {
        display: flex;
        flex-direction: row;
    }

    .tile-part:last-child {
        flex-grow: 1;
    }

    .tile-head {
        text-align: center;
        font-weight: 800;
        font-size: var(--font-header);

        border-radius: 0.8rem 0.8rem 0px 0px;
        border-bottom: 0.2rem dashed var(--fg);

        background: repeating-linear-gradient(
          -45deg,
          var(--dim),
          var(--dim) 10px,
          var(--dimmer) 10px,
          var(--dimmer) 20px
        );
    }

    .tile-part:first-child {
        border-bottom: 0.2rem dashed var(--fg);
    }

    .tile-l {
        display: flex;
        align-items: center;
        border-right: 0.2rem dashed var(--fg);
        padding: 0rem 0.3rem 0rem 0.2rem;
        font-weight: 500;
        color: var(--sc);
        text-shadow: 1px 1px 2px var(--sc);
        background-color: rgb(from var(--dim) r g b / 50%);
    }

    .tlb {
        border-bottom-left-radius: 0.8rem;
    }

    .tile-r {
        padding: 0.2rem 0rem 0.2rem 0.4rem;
    }

    .item {
        display: flex;
        flex-direction: row;
        align-items: center;
        gap: 0.4rem;
    }
</style>
