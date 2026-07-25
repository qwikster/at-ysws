<script>
import { page } from "$app/state";
import { onMount } from "svelte";

let user = null;

onMount(async () => {
  const res = await fetch(`/api/users/${page.params.id}`);
  user = await res.json()
})
</script>

you are user ${page.params.id}
