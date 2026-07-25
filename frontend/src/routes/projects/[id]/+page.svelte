<script>
import { page } from "$app/state";
import { onMount } from "svelte";

let project = null;

onMount(async () => {
  const res = await fetch(`/api/projects/${page.params.id}`);
  project = await res.json()
})
</script>

your project id is ${page.params.id}
