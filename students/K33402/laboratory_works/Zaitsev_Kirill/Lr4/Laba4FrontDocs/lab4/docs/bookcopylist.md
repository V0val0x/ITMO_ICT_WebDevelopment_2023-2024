```vue
<script setup>
import {onMounted, ref} from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import {TokenStore} from "@/stores/TokenStore";

const Token = TokenStore()
const  bookcopys = ref([])

function getBooks(){
  instance.get('/system/book-copy/', {
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 200){
          bookcopys.value = response.data
        }
      }
  ).catch(error => console.log(error))
}

function deleteBook(id){
  instance.delete(`/system/book-copy/${id}/`, {
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 204){
          getBooks()
        }
      }
  ).catch(error => console.log(error))
}

onMounted(() => {getBooks()})

</script>

<template>
  <div class="d-flex align-center flex-column ga-10">
    <h2>Экземпляры книг</h2>
    <template v-for="bookcopy in bookcopys" :key="bookcopy.id">
      <v-card
          width="400"
          :title="bookcopy.book.name"
          :subtitle="bookcopy.cipher"
          :text = "bookcopy.publishing_year"
      ><v-card-actions>
        <v-btn @click="router.push('/book-copies/' + bookcopy.id)">
          Изменить
        </v-btn>
        <v-btn @click="deleteBook(bookcopy.id)">
          Удалить
        </v-btn>
      </v-card-actions></v-card>
    </template>
    <v-btn @click="router.push('/add-book-copy')">Добавить</v-btn>
  </div>
</template>

<style scoped>
</style>
```