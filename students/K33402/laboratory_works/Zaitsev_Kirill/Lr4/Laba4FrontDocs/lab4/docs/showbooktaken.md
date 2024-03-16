```vue
<script setup>
import {onMounted, ref} from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import {TokenStore} from "@/stores/TokenStore";

const Token = TokenStore()

const takens = ref([])


function getPaper(){
  instance.get(`/system/reader/${router.currentRoute.value.params.id}/show_taken`, {
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 200){
          takens.value = response.data
        }
      }
  ).catch(error => console.log(error))
}

onMounted(() => {
  getPaper()
})


</script>
<template>
  <div class="d-flex align-center flex-column ga-10">
    <template v-for="taken in takens" :key="taken.id">
      <v-card
          width="600"
          :title="taken.book_copy.book.name"
          :subtitle="`${taken.take_date} - ${taken.return_date}`"
      ><v-card-actions>

      </v-card-actions></v-card>
    </template>
  </div>
</template>

<style scoped>

</style>
```