package main

import (
	"fmt"
	. "github.com/mndrix/golog"
)


func main(){
	m := NewMachine().Consult(`
		promedio(modalidaddeposgrado,UniversidadDistrital,pregrado,3.8). 
		promedio(modalidaddepasantia,UniversidadDistrital,pregrado,4.0). 
		porcentajecursadonecesario(modalidaddeposgrado,UniversidadDistrital,pregrado,80). 
		posiblemodalidaddegrado(A,PROMEDIO,PORCENTAJECURSADO):-PROMEDIO@>=3.8,PORCENTAJECURSADO@>=80,A=posgrado.
		materia(A,NOTA):-NOTA@>=3,A=aprobada.
		`)
	//fmt.Println(m.CanProve(`posiblemodalidaddegrado(A,1000,1000).`))
	if m.CanProve("posiblemodalidaddegrado(A,5,100).") {
		fmt.Println(true)
	}
	solutions := m.ProveAll(`posiblemodalidaddegrado(A,5,100).`)
	for _, solution := range solutions {
		fmt.Println(solution.ByName_("A"))
	}
	solutions2 := m.ProveAll(`materia(A,4).`)
	for _, solution2 := range solutions2 {
		fmt.Println(solution2.ByName_("A"))
	}
	//solutions := m.ProveAll("promedio(Y,UniversidadDistrital,pregrado,X).")
	//for _, solution := range solutions {
		//fmt.Println(solution.ByName_("X"))
	//}
}


