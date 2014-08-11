#ifndef DPAnalysis_H
#define DPAnalysis_H
// -*- C++ -*-
//
// Package:    DPAnalysis
// Class:      DPAnalysis
// 
/**\class DPAnalysis DPAnalysis.cc Exotica/DPAnalysis/src/DPAnalysis.h

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Shih-Chuan Kao
//         Created:  Thu Sep 29 05:26:22 CDT 2011
// $Id$
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/Framework/interface/ESHandle.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "DataFormats/Common/interface/TriggerResults.h"
#include "FWCore/Common/interface/TriggerNames.h"
#include "DataFormats/HLTReco/interface/TriggerObject.h"
#include "DataFormats/HLTReco/interface/TriggerEvent.h"
#include "DataFormats/Math/interface/deltaR.h"

#include "DataFormats/ParticleFlowCandidate/interface/PFCandidate.h"
#include "DataFormats/ParticleFlowReco/interface/PFBlock.h"
#include "DataFormats/ParticleFlowReco/interface/PFBlockElement.h"
#include "DataFormats/JetReco/interface/PFJetCollection.h"
#include "DataFormats/METReco/interface/PFMETCollection.h"
#include "DataFormats/EgammaCandidates/interface/Photon.h"

//EXTRA FOR DXY

#include "Geometry/TrackerGeometryBuilder/interface/TrackerGeometry.h"
#include "TrackingTools/MaterialEffects/interface/PropagatorWithMaterial.h"
#include "DataFormats/GeometrySurface/interface/BoundCylinder.h"
#include "DataFormats/GeometrySurface/interface/SimpleCylinderBounds.h"
#include "DataFormats/GeometrySurface/interface/BoundDisk.h"
#include "TrackingTools/PatternTools/interface/ClosestApproachInRPhi.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"

// AOD Objects
#include "DataFormats/JetReco/interface/PFJetCollection.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "DataFormats/BeamSpot/interface/BeamSpot.h"

#include "DataFormats/METReco/interface/PFMET.h"
#include "DataFormats/METReco/interface/PFMETCollection.h"

#include "DataFormats/EgammaCandidates/interface/PhotonFwd.h"
#include "DataFormats/EgammaCandidates/interface/Photon.h"

#include "DataFormats/GsfTrackReco/interface/GsfTrack.h"
#include "DataFormats/EgammaCandidates/interface/ElectronFwd.h"
#include "DataFormats/EgammaCandidates/interface/GsfElectronFwd.h"

#include "DataFormats/MuonReco/interface/MuonFwd.h"
#include "DataFormats/MuonReco/interface/Muon.h"

#include "DataFormats/METReco/interface/BeamHaloSummary.h"

#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"

// L1 Trigger 
#include "CondFormats/L1TObjects/interface/L1GtTriggerMenu.h"
#include "CondFormats/DataRecord/interface/L1GtTriggerMenuRcd.h"
#include "CondFormats/DataRecord/interface/EcalIntercalibConstantsRcd.h"
#include "DataFormats/L1GlobalTrigger/interface/L1GlobalTriggerReadoutSetupFwd.h"
#include "DataFormats/L1GlobalTrigger/interface/L1GlobalTriggerReadoutSetup.h"
#include "DataFormats/L1GlobalTrigger/interface/L1GlobalTriggerReadoutRecord.h"

// for ECAL cluster
#include "DataFormats/EgammaReco/interface/BasicCluster.h"
#include "DataFormats/EgammaReco/interface/BasicClusterFwd.h"
#include "DataFormats/EgammaReco/interface/SuperCluster.h"
#include "DataFormats/EgammaReco/interface/SuperClusterFwd.h"
#include "DataFormats/EcalRecHit/interface/EcalRecHitCollections.h"
#include "RecoEcal/EgammaCoreTools/interface/EcalClusterTools.h"

#include "CondFormats/EcalObjects/interface/EcalIntercalibConstants.h"
#include "CondFormats/DataRecord/interface/EcalIntercalibConstantsRcd.h"
#include "CondFormats/EcalObjects/interface/EcalADCToGeVConstant.h"
#include "CondFormats/DataRecord/interface/EcalADCToGeVConstantRcd.h"
#include "CalibCalorimetry/EcalLaserCorrection/interface/EcalLaserDbService.h"
#include "CalibCalorimetry/EcalLaserCorrection/interface/EcalLaserDbRecord.h"

// for CSC Segment
#include "DataFormats/CSCRecHit/interface/CSCSegmentCollection.h"
#include "Geometry/Records/interface/MuonGeometryRecord.h"
#include "DataFormats/METReco/interface/CSCHaloData.h"

// For DT Segment
#include "DataFormats/DTRecHit/interface/DTRecSegment4DCollection.h"


// TrackingRecHit to replace CSCSegment
#include "DataFormats/TrackingRecHit/interface/TrackingRecHitFwd.h"
#include "DataFormats/Common/interface/OwnVector.h"

// Calibration services
//#include "Geometry/CaloGeometry/interface/CaloGeometry.h"
//#include "Geometry/Records/interface/CaloGeometryRecord.h"

//#include "CondFormats/EcalObjects/interface/EcalIntercalibConstants.h"
//#include "CondFormats/DataRecord/interface/EcalIntercalibConstantsRcd.h"
//#include "CondFormats/EcalObjects/interface/EcalADCToGeVConstant.h"
//#include "CondFormats/DataRecord/interface/EcalADCToGeVConstantRcd.h"
//#include "CalibCalorimetry/EcalLaserCorrection/interface/EcalLaserDbService.h"
//#include "CalibCalorimetry/EcalLaserCorrection/interface/EcalLaserDbRecord.h"
#include "RecoEcal/EgammaCoreTools/interface/EcalTools.h"
//#include "CalibCalorimetry/EcalTiming/interface/timeVsAmpliCorrector.h"

// JEC uncerntainties
#include "CondFormats/JetMETObjects/interface/JetCorrectorParameters.h"
#include "CondFormats/JetMETObjects/interface/JetCorrectionUncertainty.h"
#include "JetMETCorrections/Objects/interface/JetCorrectionsRecord.h"

// for PAT Object selections
#include "DataFormats/PatCandidates/interface/PATObject.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/Photon.h"
#include "DataFormats/EgammaCandidates/interface/Photon.h"

#include "RecoEgamma/EgammaTools/interface/ConversionTools.h"

//#include "EGamma/EGammaAnalysisTools/src/PFIsolationEstimator.cc"
#include "PFIsolationEstimator.h"
#include <algorithm>

// global tracking geometry
//#include "Geometry/Records/interface/GlobalTrackingGeometryRecord.h"
//#include "Geometry/CommonDetUnit/interface/GlobalTrackingGeometry.h"

// PU SummeryInfo
#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h" 

#include <TMath.h>
#include "TFile.h"
#include "TTree.h"

#include "Ntuple.h"
#include "GenStudy.h"

#include <Math/VectorUtil.h>

using namespace std ;

//
// class declaration
//

typedef std::pair<reco::SuperClusterRef, float> ParticleSC  ;

struct PhoInfo {

  double t    ;
  double dt   ;
  double nchi2  ;
  double fSpike ;
  double maxSX  ;
  int    nxtals ;  
  int    nBC    ;

} ;

struct VtxInfo {

  int nTracks ;
  double ndof ;
  double chi2 ;
  double x ;
  double y ;
  double z ;
  double dx ;
  double dy ;
  double dz ;
  double ht ;
  
} ;

struct TrkInfo {

  double dz ;
  double dsz ;
  double d0 ;
  double pt ;
  double vz ;
  double vr ;

} ;

typedef const pat::Jet pat_Jet ;

class ConversionTools ;

//Extra class for DXY
class TangentApproachInRPhi : public ClosestApproachOnHelices {

 public:

  TangentApproachInRPhi() {status_ = false; intersection_ = false;}

  virtual bool calculate(const TrajectoryStateOnSurface & sta,
                         const TrajectoryStateOnSurface & stb);

  virtual bool calculate(const FreeTrajectoryState & sta,
                         const FreeTrajectoryState & stb);

  virtual bool status() const {return status_;}

  /**
   * Returns the two PCA on the trajectories.
   */
  virtual std::pair<GlobalPoint, GlobalPoint> points() const;

  /** Returns not only the points, but the full GlobalTrajectoryParemeters
   *  at the points of closest approach */
  std::pair <GlobalTrajectoryParameters, GlobalTrajectoryParameters >
    trajectoryParameters () const;

  /** arithmetic mean of the two points of closest approach */
  virtual GlobalPoint crossingPoint() const;

  /** distance between the two points of closest approach in 3D */
  virtual float distance() const;

  /** signed distance between two points of closest approach in r-phi plane (-ive if circles intersect) */
  float perpdist() const;

  /**
   *  Clone method
   */
  virtual TangentApproachInRPhi * clone() const {
    return new TangentApproachInRPhi(* this);
  }

 private:
  
  bool calculate(const TrackCharge & chargeA,
                 const GlobalVector & momentumA,
                 const GlobalPoint & positionA,
                 const TrackCharge & chargeB,
                 const GlobalVector & momentumB,
                 const GlobalPoint & positionB,
                 const MagneticField& magField);

  // given the old Parameters, and a new GlobalPoint,
  // we return the full new GlobalTrajectoryParameters at the
  // Point.
  GlobalTrajectoryParameters trajectoryParameters ( const GlobalPoint & newpt,
                                                    const GlobalTrajectoryParameters & oldpar ) const;

  // Computes center coordinates and unsigned radius of circle;
  void circleParameters(const TrackCharge& charge,
                        const GlobalVector& momemtum,
			const GlobalPoint& position,
                        double& xc, double& yc, double& r,
			const MagneticField& magField) const;

  // Computes crossing points of 2 circles with centres (cx_i, cy_i)
  // and unsigned radii r_i.
  // Two cases: - circles have one or two intersection points;
  //              return value = 1;
  //            - circles do not cross; computes point of closest approach
  //              on each circle; return value = 2;
  // if the calculation fails (e.g. concentric circles), return value = 0;

  int transverseCoord(double cxa, double cya, double ra,
                      double cxb, double cyb, double rb,
                      double & xg1, double & yg1,
                      double & xg2, double & yg2) const;

  // Computes z-coordinate on helix at given transverse coordinates
  double zCoord(const GlobalVector& mom, const GlobalPoint& pos,
                double r, double xc, double yc, double xg, double yg) const;

 private:
  bool status_;
  GlobalPoint posA, posB;
  GlobalTrajectoryParameters paramA, paramB;
  bool intersection_;
};

bool TangentApproachInRPhi::calculate(const TrajectoryStateOnSurface & sta,
                                      const TrajectoryStateOnSurface & stb)
{
  TrackCharge chargeA = sta.charge(); TrackCharge chargeB = stb.charge();
  GlobalVector momentumA = sta.globalMomentum();
  GlobalVector momentumB = stb.globalMomentum();
  GlobalPoint positionA = sta.globalPosition();
  GlobalPoint positionB = stb.globalPosition();
  paramA = sta.globalParameters();
  paramB = stb.globalParameters();

  return calculate(chargeA, momentumA, positionA, chargeB, momentumB, positionB,
                   sta.freeState()->parameters().magneticField());
}


bool TangentApproachInRPhi::calculate(const FreeTrajectoryState & sta,
                                      const FreeTrajectoryState & stb)
{
  TrackCharge chargeA = sta.charge(); TrackCharge chargeB = stb.charge();
  GlobalVector momentumA = sta.momentum();
  GlobalVector momentumB = stb.momentum();
  GlobalPoint positionA = sta.position();
  GlobalPoint positionB = stb.position();
  paramA = sta.parameters();
  paramB = stb.parameters();

  return calculate(chargeA, momentumA, positionA, chargeB, momentumB, positionB,
                   sta.parameters().magneticField());
}

pair<GlobalPoint, GlobalPoint> TangentApproachInRPhi::points() const
{
  if (!status_)
    throw cms::Exception("TrackingTools/PatternTools","TangentApproachInRPhi::could not compute track crossing. Check status before calling this metho\
d!");  
  return  pair<GlobalPoint, GlobalPoint> (posA, posB);
}


GlobalPoint
TangentApproachInRPhi::crossingPoint() const
{
  if (!status_)
    throw cms::Exception("TrackingTools/PatternTools","TangentApproachInRPhi::could not compute track crossing. Check status before calling this metho\
d!");
  return GlobalPoint((posA.x() + posB.x())/2.,
                     (posA.y() + posB.y())/2.,
                     (posA.z() + posB.z())/2.);
}

float TangentApproachInRPhi::distance() const
{
  if (!status_)
    throw cms::Exception("TrackingTools/PatternTools","TangentApproachInRPhi::could not compute track crossing. Check status before calling this metho\
d!");
  return (posB - posA).mag();
}

float TangentApproachInRPhi::perpdist() const
{
  if (!status_)
    throw cms::Exception("TrackingTools/PatternTools","TangentApproachInRPhi::could not compute track crossing. Check status before calling this metho\
d!");

  float perpdist = (posB - posA).perp();

  if (intersection_) {
    perpdist = -perpdist;
  }

  return perpdist;

}

bool TangentApproachInRPhi::calculate(const TrackCharge & chargeA,
                                      const GlobalVector & momentumA,
                                      const GlobalPoint & positionA,
                                      const TrackCharge & chargeB,
                                      const GlobalVector & momentumB,
                                      const GlobalPoint & positionB,
                                      const MagneticField& magField)
{

  // centres and radii of track circles
  double xca, yca, ra;
  circleParameters(chargeA, momentumA, positionA, xca, yca, ra, magField);
  double xcb, ycb, rb;
  circleParameters(chargeB, momentumB, positionB, xcb, ycb, rb, magField);

  // points of closest approach in transverse plane
  double xg1, yg1, xg2, yg2;
  int flag = transverseCoord(xca, yca, ra, xcb, ycb, rb, xg1, yg1, xg2, yg2);
  if (flag == 0) {
    status_ = false;
    return false;
  }

  double xga, yga, zga, xgb, ygb, zgb;

  if (flag == 1) {
    intersection_ = true;
  }
  else {
    intersection_ = false;
  }

  // one point of closest approach on each track in transverse plane
  xga = xg1; yga = yg1;
  zga = zCoord(momentumA, positionA, ra, xca, yca, xga, yga);
  xgb = xg2; ygb = yg2;
  zgb = zCoord(momentumB, positionB, rb, xcb, ycb, xgb, ygb);

  posA = GlobalPoint(xga, yga, zga);
  posB = GlobalPoint(xgb, ygb, zgb);
  status_ = true;
  return true;
}

pair <GlobalTrajectoryParameters, GlobalTrajectoryParameters>
  TangentApproachInRPhi::trajectoryParameters () const
{
  if (!status_)
    throw cms::Exception("TrackingTools/PatternTools","TangentApproachInRPhi::could not compute track crossing. Check status before calling this metho\
d!");
  pair <GlobalTrajectoryParameters, GlobalTrajectoryParameters>
    ret ( trajectoryParameters ( posA, paramA ),
          trajectoryParameters ( posB, paramB ) );
  return ret;
}

GlobalTrajectoryParameters TangentApproachInRPhi::trajectoryParameters (
                                                                        const GlobalPoint & newpt, const GlobalTrajectoryParameters & oldgtp ) const
{
  // First we need the centers of the circles.
  double xc, yc, r;
  circleParameters( oldgtp.charge(), oldgtp.momentum(),
                    oldgtp.position(), xc, yc, r, oldgtp.magneticField()  );

  // now we do a translation, move the center of circle to (0,0,0).
  double dx1 = oldgtp.position().x() - xc;
  double dy1 = oldgtp.position().y() - yc;
  double dx2 = newpt.x() - xc;
  double dy2 = newpt.y() - yc;

  // now for the angles:
  double cosphi = ( dx1 * dx2 + dy1 * dy2 ) /
    ( sqrt ( dx1 * dx1 + dy1 * dy1 ) * sqrt ( dx2 * dx2 + dy2 * dy2 ));
  double sinphi = - oldgtp.charge() * sqrt ( 1 - cosphi * cosphi );

  // Finally, the new momenta:
  double px = cosphi * oldgtp.momentum().x() - sinphi * oldgtp.momentum().y();
  double py = sinphi * oldgtp.momentum().x() + cosphi * oldgtp.momentum().y();
  
  GlobalVector vta ( px, py, oldgtp.momentum().z() );
  GlobalTrajectoryParameters gta( newpt , vta , oldgtp.charge(), &(oldgtp.magneticField()) );
  return gta;
}

void
TangentApproachInRPhi::circleParameters(const TrackCharge& charge,
                                        const GlobalVector& momentum,
                                        const GlobalPoint& position,
                                        double& xc, double& yc, double& r,
                                        const MagneticField& magField)
const
{

  // compute radius of circle
  /** temporary code, to be replaced by call to curvature() when bug
   *  is fixed.
   */
  //   double bz = MagneticField::inInverseGeV(position).z();
  double bz = magField.inTesla(position).z() * 2.99792458e-3;
  
  // signed_r directed towards circle center, along F_Lorentz = q*v X B
  double signed_r = charge*momentum.transverse() / bz;
  r = abs(signed_r);
  /** end of temporary code
   */

  // compute centre of circle
  double phi = momentum.phi();
  xc = signed_r*sin(phi) + position.x();
  yc = -signed_r*cos(phi) + position.y();

}

int
TangentApproachInRPhi::transverseCoord(double cxa, double cya, double ra,
                                       double cxb, double cyb, double rb,
                                       double & xg1, double & yg1,
                                       double & xg2, double & yg2) const
{
  int flag = 0;
  double x1, y1, x2, y2;

  // new reference frame with origin in (cxa, cya) and x-axis
  // directed from (cxa, cya) to (cxb, cyb)

  double d_ab = sqrt((cxb - cxa)*(cxb - cxa) + (cyb - cya)*(cyb - cya));
  if (d_ab == 0) { // concentric circles
    return 0;
  }
  // elements of rotation matrix
  double u = (cxb - cxa) / d_ab;
  double v = (cyb - cya) / d_ab;

  // conditions for circle intersection
  if (d_ab <= ra + rb && d_ab >= abs(rb - ra)) {

    // circles cross each other
    //     flag = 1;
    //
    //     // triangle (ra, rb, d_ab)
    //     double cosphi = (ra*ra - rb*rb + d_ab*d_ab) / (2*ra*d_ab);
    //     double sinphi2 = 1. - cosphi*cosphi;
    //     if (sinphi2 < 0.) { sinphi2 = 0.; cosphi = 1.; }
    //
    //     // intersection points in new frame
    //     double sinphi = sqrt(sinphi2);
    //     x1 = ra*cosphi; y1 = ra*sinphi; x2 = x1; y2 = -y1;

    //circles cross each other, but take tangent points anyway
    flag = 1;

    // points of closest approach in new frame
    // are on line between 2 centers
    x1 = ra; y1 = 0; x2 = d_ab - rb; y2 = 0;


  }
  else if (d_ab > ra + rb) {
    // circles are external to each other
    flag = 2;

    // points of closest approach in new frame
    // are on line between 2 centers
    x1 = ra; y1 = 0; x2 = d_ab - rb; y2 = 0;
  }
  else if (d_ab < abs(rb - ra)) {

    // circles are inside each other
    flag = 2;

    // points of closest approach in new frame are on line between 2 centers
    // choose 2 closest points
    double sign = 1.;
    if (ra <= rb) sign = -1.;
    x1 = sign*ra; y1 = 0; x2 = d_ab + sign*rb; y2 = 0;
  }
  else {
    return 0;
  }

  // intersection points in global frame, transverse plane
  xg1 = u*x1 - v*y1 + cxa; yg1 = v*x1 + u*y1 + cya;
  xg2 = u*x2 - v*y2 + cxa; yg2 = v*x2 + u*y2 + cya;

  return flag;
}


double
TangentApproachInRPhi::zCoord(const GlobalVector& mom,
                              const GlobalPoint& pos,
                              double r, double xc, double yc,
                              double xg, double yg) const
{

  // starting point
  double x = pos.x(); double y = pos.y(); double z = pos.z();
  double px = mom.x(); double py = mom.y(); double pz = mom.z();

  // rotation angle phi from starting point to crossing point (absolute value)
  // -- compute sin(phi/2) if phi smaller than pi/4,
  // -- cos(phi) if phi larger than pi/4
  double phi = 0.;
  double sinHalfPhi = sqrt((x-xg)*(x-xg) + (y-yg)*(y-yg))/(2*r);
  if (sinHalfPhi < 0.383) { // sin(pi/8)
    phi = 2*asin(sinHalfPhi);
  }
  else {
    double cosPhi = ((x-xc)*(xg-xc) + (y-yc)*(yg-yc))/(r*r);
    if (std::abs(cosPhi) > 1) cosPhi = (cosPhi > 0 ? 1 : -1);
    phi = abs(acos(cosPhi));
  }
  // -- sign of phi
  double signPhi = ((x - xc)*(yg - yc) - (xg - xc)*(y - yc) > 0) ? 1. : -1.;

  // sign of track angular momentum
  // if rotation is along angular momentum, delta z is along pz
  double signOmega = ((x - xc)*py - (y - yc)*px > 0) ? 1. : -1.;

  // delta z
  // -- |dz| = |cos(theta) * path along helix|
  //         = |cos(theta) * arc length along circle / sin(theta)|
  double dz = signPhi*signOmega*(pz/mom.transverse())*phi*r;

  return z + dz;
}





class DPAnalysis : public edm::EDAnalyzer {
   public:
      explicit DPAnalysis(const edm::ParameterSet&);
      ~DPAnalysis();

      //EXTRA for Dxy
      GlobalTrajectoryParameters getGlobalTrajectoryParameters(const RefToBase<reco::Track>& track);
      GlobalTrajectoryParameters transTrajectoryParameters (const GlobalPoint & newpt,
                                                            const GlobalTrajectoryParameters & oldgtp ) const;
      
      bool getTrackImpactPosition(const RefToBase<reco::Track>& tk_ref,
                                  const TrackerGeometry* trackerGeom, const MagneticField* magField,
                                  math::XYZPoint& ew);

      virtual void analyze(const edm::Event&, const edm::EventSetup&);

      bool EventSelection( const edm::Event& iEvent, const edm::EventSetup& iSetup );

      void CSCHaloCleaning( const edm::Event& iEvent, vector<const reco::Photon*>& selectedPhotons )  ;

      bool L1TriggerSelection( const edm::Event& iEvent, const edm::EventSetup& iSetup ) ;

      void TriggerTagging( edm::Handle<edm::TriggerResults> triggers, const edm::TriggerNames& trgNameList, int RunID, vector<int>& firedTrig ) ;
      bool TriggerSelection( edm::Handle<edm::TriggerResults> triggers, vector<int> firedTrig ) ;
      //bool TriggerSelection( const edm::Event& iEvent, int RunID ) ;
 
      template<typename object>
      bool GetTrgMatchObject( object, const edm::Event& iEvent, edm::InputTag inputProducer_ ) ;

      void Track_Z0( edm::Handle<reco::TrackCollection> trks ) ;
      bool VertexSelection( edm::Handle<reco::VertexCollection> vtx ) ;

      bool PhotonSelection(  edm::Handle<reco::PhotonCollection> photons, edm::Handle<EcalRecHitCollection> recHitsEB, edm::Handle<EcalRecHitCollection> recHitsEE, edm::Handle<reco::TrackCollection> tracks, vector<const reco::Photon*>& selectedPhotons, const edm::Event& iEvent,const edm::EventSetup& iSetup  ) ;

      pair<double,double> ClusterTime( reco::SuperClusterRef scRef, edm::Handle<EcalRecHitCollection> recHitsEB, edm::Handle<EcalRecHitCollection> recHitsEE ) ;
      void ClusterTime( reco::SuperClusterRef scRef, edm::Handle<EcalRecHitCollection> recHitsEB, edm::Handle<EcalRecHitCollection> recHitsEE, PhoInfo& phoTmp, bool useAllClusters = false ) ;
      //void ClusterTime( reco::SuperClusterRef scRef, edm::Handle<EcalRecHitCollection> recHitsEB, edm::Handle<EcalRecHitCollection> recHitsEE, double& aveTime, double& aveTimeErr, double& nChi2, bool useAllClusters = false ) ;

      //double HLTMET( edm::Handle<reco::PFJetCollection> jets, vector<const reco::Muon*>& selectedMuons, bool addMuon = false ) ;

      bool JetSelection( edm::Handle<reco::PFJetCollection> jets, vector<const reco::Photon*>& selectedPhotons, vector<const reco::PFJet*>& selectedJets ) ;

      bool JetSelection( edm::Handle<std::vector<pat::Jet> > patjets, vector<const reco::Photon*>& selectedPhotons, vector< pat_Jet* >& selectedJets_ ) ;

      vector<double> JECUncertainty( double jetpt, double jeteta, JetCorrectionUncertainty* unc ) ;
      vector<double> JECUncertainty( double jetpt, double jeteta ) ;
      void JERUncertainty( edm::Handle< std::vector<pat::Jet> > patjets )  ;

      bool ElectronSelection( edm::Handle<reco::GsfElectronCollection> electrons, 
                              vector<const reco::GsfElectron*>& selectedElectrons ) ;
      bool MuonSelection( edm::Handle<reco::MuonCollection> muons, vector<const reco::Muon*>& selectedMuons ) ;
      void PrintTriggers( const edm::Event& iEvent ) ;

      bool sMinorSelection( vector<const reco::Photon*>& selectedPhotons,  edm::Handle<EcalRecHitCollection> recHitsEB,     
                              edm:: Handle<EcalRecHitCollection> recHitsEE ) ;

      bool IsoPhotonSelection( vector<const reco::Photon*>& selectedPhotons ) ; 

      bool GammaJetVeto( vector<const reco::Photon*>& selectedPhotons, vector<const reco::PFJet*>& selectedJets) ;

      bool BeamHaloMatch( edm::Handle<CSCSegmentCollection> cscSeg, vector<const reco::Photon*>& selectedPhotons, const edm::EventSetup& iSetup ) ;
      bool BeamHaloMatch( edm::OwnVector<TrackingRecHit> rhits, vector<const reco::Photon*>& selectedPhotons, const edm::EventSetup& iSetup ) ;
      bool CosmicRayMatch( edm::Handle<reco::MuonCollection> muons, vector<const reco::Photon*>& selectedPhotons ) ;

      bool CosmicRayMatch( edm::Handle<DTRecSegment4DCollection> dtSeg, vector<const reco::Photon*>& selectedPhotons, const EventSetup& iSetup );

      bool ConversionVeto( const reco::Photon* thePhoton ) ;
      double RhoCorrection( int type , double eta ) ;
      void PhotonPFIso( std::vector<const reco::Photon*> thePhotons, const reco::PFCandidateCollection* pfParticlesColl, reco::VertexRef vtxRef, edm::Handle< reco::VertexCollection > vtxColl ) ;

   private:

      // Computes center coordinates and unsigned radius of circle;
      void circleParameters(const TrackCharge& charge,
                            const GlobalVector& momemtum,
                            const GlobalPoint& position,
                            double& xc, double& yc, double& r,
                            const MagneticField& magField) const;

      Ntuple leaves ;

      TTree *theTree;
//      TTree *thePUTree;
      TTree *CutFlowTree;
      TH1   *h_z0 ;
      TH1   *hPU ;

      TFile *theFile;
      GenStudy *gen ; 

      // ----------member data ---------------------------
      string rootFileName;
      std::vector<string> triggerPatent ;
      bool isData ;
      bool isRECO ;
      bool L1Select ;
      string l1GTSource ;
      double tau ;

      edm::InputTag trigSource;
      edm::InputTag trigEvent;
      edm::InputTag pvSource;
      edm::InputTag beamSpotSource;
      edm::InputTag muonSource;
      edm::InputTag electronSource;
      edm::InputTag photonSource;
      edm::InputTag metSource;
      edm::InputTag type1metSource;
      edm::InputTag jetSource;
      edm::InputTag patJetSource;
      edm::InputTag trackSource;

      edm::InputTag EBRecHitCollection;
      edm::InputTag EERecHitCollection;
      edm::InputTag DTSegmentTag ;
      edm::InputTag CSCSegmentTag ;
      edm::InputTag cscHaloTag ;
      edm::InputTag staMuons ;

      edm::InputTag pileupSource ;
      edm::ESHandle<EcalIntercalibConstants> ical;
      edm::ESHandle<EcalADCToGeVConstant> agc;
      edm::ESHandle<EcalLaserDbService> laser;
      edm::ESHandle<CaloGeometry> pGeometry ;
      const CaloGeometry * theGeometry ;
      //edm::ESHandle<GlobalTrackingGeometry> trackingGeometry;


      // PFIso use
      edm::Handle<double> rho_ ;   
      double rhoIso ;
      PFIsolationEstimator isolator;


      // photon conversion veto 
      const reco::BeamSpot* beamspot ;
      edm::Handle<reco::ConversionCollection> hConversions;
      edm::Handle<reco::BeamSpot> bsHandle;
      edm::Handle<reco::GsfElectronCollection> electrons;

      // For JES Uncertainty
      JetCorrectionUncertainty *jecUnc ;

      std::vector<double> muonCuts ;
      std::vector<double> electronCuts ;
      std::vector<double> photonCuts ;
      std::vector<double> photonIso ;
      std::vector<double> metCuts ;
      std::vector<double> jetCuts ; 
      std::vector<double> vtxCuts ; 

      //std::vector<const reco::PFJet*> selectedJets ;
      std::vector<pat_Jet*> selectedJets ;
      std::vector<const reco::GsfElectron*> selectedElectrons ;
      std::vector<const reco::Muon*> selectedMuons ;
      std::vector<const reco::Photon*> selectedPhotons ;

      bool passEvent ;
      int PU_TrueNumInter; 
//      int PU_TrueNumInter2; 
//      int test ; 
      int counter[12] ; 
      int gcounter[7] ;
      float sMin_ ;
      int runID_ ;

//      timeCorrector theTimeCorrector_;
      edm::Timestamp eventTime ;

      std::vector<int> firedTrig ;
      int targetTrig ;
      //std::vector<int> firedTrigID ;
      ///string TriggerName ;
      bool passL1 ;
      bool passHLT ;

      bool debugT ; 

      const MagneticField * theMagField;
};

#endif
