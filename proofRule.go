package main

import (
	"fmt"
	. "github.com/mndrix/golog"
)


func main(){
	m := NewMachine().Consult(`
			estudiante(A,PROMEDIO):-PROMEDIO==5,A=excelente.
			materia(A,NOTA):-NOTA@>=3,A=aprobada.
			materia(A,NOTA):-NOTA@=<3,A=reprobada.
			estado(A,NUMEROMATERIASPERDIDAS):-NUMEROMATERIASPERDIDAS@>=3,A=pruebaacademica.
		`)
	//fmt.Println(m.CanProve(`posiblemodalidaddegrado(A,1000,1000).`))
	solutions2 := m.ProveAll(`estado(A,2).`)
	for _, solution2 := range solutions2 {
		fmt.Println(solution2.ByName_("A"))
	}
	//solutions := m.ProveAll("promedio(Y,UniversidadDistrital,pregrado,X).")
	//for _, solution := range solutions {
		//fmt.Println(solution.ByName_("X"))
	//}
}


