```vue
<script setup>
import {onMounted, ref} from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import {TokenStore} from "@/stores/TokenStore";

const Token = TokenStore()
const  booktakes = ref([])

function getBooktakes(){
  instance.get('/system/book-take/', {
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 200){
          booktakes.value = response.data
        }
      }
  ).catch(error => console.log(error))
}

function deleteBooktake(id){
  instance.delete(`/system/book-take/${id}/`, {
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 204){
          getBooktakes()
        }
      }
  ).catch(error => console.log(error))
}

onMounted(() => {getBooktakes()})

</script>

<template>
  <div class="d-flex align-center flex-column ga-10">
    <h2>Взятые книги</h2>
    <v-btn @click="router.push('/book-takes/last_month')">
      Смотреть только взятые более месяца назад
    </v-btn>
    <template v-for="booktake in booktakes" :key="booktake.id">
      <v-card
          width="400"
          :title="`${booktake.book_copy.book.name} взята ${booktake.reader.full_name}`"
          :text = "`${booktake.take_date} - ${booktake.return_date}`"
      ><v-card-actions>
        <v-btn @click="router.push('/book-takes/' + booktake.id)">
          Изменить
        </v-btn>
        <v-btn @click="deleteBooktake(booktake.id)">
          Удалить
        </v-btn>
      </v-card-actions></v-card>
    </template>
    <v-btn @click="router.push('/add-book-take')">Добавить</v-btn>
  </div>
</template>

<style scoped>
</style>
```