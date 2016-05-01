--====== 
-- name: effects2.elm
-- date: 2016APR30
-- prog: pr
-- desc: working example using Effects
-- 
--       works in conjunction with backend/rserve.py 
-- 
-- src : <http://www.elm-tutorial.org/040_effects/effects_2.html
--======


import Html
import Html.Events as Events
import Http
import Task
import Debug
import Effects


-- TYPES
type Action = 
    NoOp | 
    Refresh | 
    OnRefresh (Result Http.Error String)


type alias Model = String


--VIEW
view : Signal.Address Action -> Model -> Html.Html
view address message = 
    Html.div [] [
        Html.button [
            Events.onClick address refresh 
	]
	[
            Html.text "Refresh"
	],
	Html.text message
    ]


actionsMailbox : Signal.Mailbox (List Action)
actionsMailbox = 
    Signal.mailbox []


oneActionAddress : Signal.Address Action
oneActionAddress = 
    Signal.forwardTo actionsMailbox.address( \action -> [action] )


httpTask : Task.Task Http.Error String
httpTask = 
    Http.getString "http://192.168.1.2:8090/"


refreshFx : Effects.Effects Action
refreshFx = 
     httpTask
         |> Task.toResult
	 |> Task.map OnRefresh
	 |> Effects.task


-- UPDATE
update : Action -> Model -> ( Model, Effects.Effects Action )
update action model = 
    case action of 
        Refresh ->
	    ( model, refreshFx )
	OnRefresh result ->
	    let
	        message = 
		    Result.withDefault "" result
            in 
	        (message, Effects.none)
	    _->
	        (model, Effects.none)
modelAndFxSignal : Signal.Signal (Model, Effects.Effects Action)
modelAndFxSignal = 
    let
        modelAndFx action (previousModel,_) = 
	    update action previousModel
	modelAndManyFx actions (previousModel, _) =
	    List.foldl modelAndFx (previousModel, Effects.none) actions
	initials = 
	    ("-", Effects.none)
    in
        Signal.foldp modelAndManyFxs initial actionsMailbox.signal


modelSignal : Signal.Signal Model
modelSignal = 
    Signal.map fst modelAndFxSignal


fxSignal : Signal.Signal (Effects.Effects Action)
fxSignal = 
    Signal.map snd modelAndFxSignal


taskSIgnal : Signal (Task.Task Effects.Never ())
taskSignal = 
    Signal.map (Effects.toTask actionsMailbox.address) fxSignal


-- MAIN
main: Signal.Signal Html.Html
main = 
    SIgnal.map (view oneActionAddress) modelSignal


-- PORTS
port runner : Signal (Task.Task Effects.Never ())
port runner = 
    taskSignal


