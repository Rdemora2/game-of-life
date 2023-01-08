<template>
  <div id="app">
    <div>
      <div v-for="line, index_row in matriz" :key="index_row" class="flex">
        <div v-for="item, index_col in line" :key="index_col">
          <Cell :row="index_row" :col="index_col" @update-life="updateCell($event)" :state="item"/>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Cell from './components/Cell'
export default {
  name: 'Vue',
  components: {
    Cell
  },
  data() {
    return {
      cols: 4,
      rows: 4,
      matriz: [
        [1,0,0,0,0,1],
        [0,0,1,0,0,0],
        [0,1,0,1,0,0],
        [0,0,1,0,0,0],
        [0,0,0,0,0,1],
        [0,0,0,1,0,1]
    ],
      newMatriz: [],
      alive: false
    }
  },
  created() {
    this.start()
  },
  methods: {
    start(){
      this.matriz = this.generateMatriz(this.matriz)
      this.exec(this.matriz)
    },
    exec(matriz){
      this.matriz = this.generateMatriz(matriz)
      setTimeout(()=>{
        this.exec(this.matriz)
      }, 200)
    },
    updateCell(event){
      if (event[2] == 0){
        this.matriz[event[0]][event[1]] = 1
      } else {
        this.matriz[event[0]][event[1]] = 0
      }
    },
    checkNeighbors(matriz, x, y){
      let testNeighbor = [
        {x: -1,y: -1}, {x: -1,y: 0}, {x: -1,y: 1}, 
        {x: 0,y: -1}, {x: 0,y: 1},
        {x: 1,y: -1}, {x: 1,y: 0}, {x: 1,y: 1}, 
      ]
      let neighbors = []
      testNeighbor.forEach((i)=>{
        if ((i['x'] + x >= 0 && i['y'] + y >= 0) && (i['x'] + x < matriz.length && i['y'] + y < matriz[0].length)){
          neighbors.push({x: i['x']+x, y: i['y']+y})
        }
      })
      let neighborsLiving = 0
      neighbors.forEach((i)=>{
        if (matriz[i['x']][i['y']] == 1){
          neighborsLiving+=1
        }
      })
      return neighborsLiving
    },
    generateMatriz(matriz){
      this.newMatriz = [
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
      ]
      for(let i = 0; i < matriz.length; i++){
        for(let j = 0; j < matriz[i].length; j++){
          const neighborsLiving = this.checkNeighbors(matriz, i, j)
          if (matriz[i][j] == 1){
            if (neighborsLiving < 2 || neighborsLiving > 3){
              this.newMatriz[i][j] = 0
            }
            else {
              this.newMatriz[i][j] = 1
            }
          }
          else {
            if (neighborsLiving == 3){
              this.newMatriz[i][j] = 1
            }
            else {
              this.newMatriz[i][j] = 0
            }
          }
        }
      }
      return this.newMatriz
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #201616;
  margin-top: 60px;
  display: flex;
  justify-content: center;
}
.flex {
  display: flex;
}
</style>